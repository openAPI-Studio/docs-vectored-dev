"""Docker & Kubernetes page: the container images and the Helm chart. Keep in
step with deploy/docker and deploy/helm in the depotex repo."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, CODE

KUBERNETES = [
    ("kubernetes", dict(
        label="Docker &amp; Kubernetes", title="Docker &amp; Kubernetes", icon="grid",
        desc="Run Depotex from its container images, on Kubernetes with the Helm chart",
        keywords=["docker", "kubernetes", "k8s", "helm", "chart", "container", "image", "distroless", "statefulset", "prometheus", "servicemonitor", "metrics",
                  "minio", "postgresql", "redis", "ingress", "secrets", "sealed secrets", "sops", "network policy", "install"],
        blocks=[
            P("Depotex ships as two container images: the server (API) and the web app. A Helm chart deploys them on Kubernetes, with PostgreSQL, Redis and MinIO built in, and each of them can be switched off for a managed service. A script creates every Kubernetes Secret outside the chart, and writes the installation's keys to a private file you keep."),

            H("The images"),
            UL([
                "**Server:** one program on a minimal base image, with no shell or package manager, plus the PostgreSQL client tools `pg_dump` and `pg_restore` 18 for [backups](backups.html) (they work with PostgreSQL 18 and older). It runs as an unprivileged user (UID 65532) and needs only its data folder and `/tmp` writable.",
                "**Web app:** the Next.js server on the same kind of base image.",
                "Neither image contains a key, licence or configuration: they come from the environment at run time.",
            ]),
            NOTE("Images aren't published to a public registry yet. Build them from the source and push them to your own registry, then set `backend.image` and `frontend.image` in the chart's values."),
            CODE("""docker build -f deploy/docker/backend.Dockerfile  -t registry.example.com/depotex-backend:1.0.0 --build-arg VERSION=1.0.0 .
docker build -f deploy/docker/frontend.Dockerfile -t registry.example.com/depotex-frontend:1.0.0 .
docker push registry.example.com/depotex-backend:1.0.0
docker push registry.example.com/depotex-frontend:1.0.0"""),

            H("Install on Kubernetes"),
            P("You need `kubectl` and Helm 3, a namespace, an ingress controller for the Depotex address, and a licence (the licence is bound to the installation ID, which you read after the first start)."),
            STEPS([
                "Create the secrets|`deploy/helm/prime-secrets.sh init -n depotex -r depotex --public-url https://depotex.example.com`. It generates every password and key, creates the Secrets in the namespace, and writes `depotex-<namespace>-<release>-install-keys.txt` (readable only by you). Add `--database-url`, `--redis-url` (or `--no-redis`) and the `--storage-*-key` options to use managed services instead of the built-in ones.",
                "Install the chart|`helm install depotex deploy/helm/depotex -n depotex -f my-values.yaml`, with at least `publicUrl` and the images. Without a licence yet, Depotex starts the setup wizard.",
                "Get the licence|`prime-secrets.sh installation-id -n depotex -r depotex` prints the installation ID (and records it in the keys file). Request a licence for it, then store it: `prime-secrets.sh license license.json -n depotex -r depotex`.",
                "Finish setup|`helm upgrade` with the same values. With the licence in the secret, Depotex sets itself up unattended from the values (administrator, database, Redis, storage). Or open the setup link from the keys file and use the wizard.",
                "After setup|Set `setup.mode: none` and upgrade once more: the server then no longer gets the setup key.",
            ]),
            WARN("Keep the keys file safe, outside the cluster. It holds `CONFIG_ENCRYPTION_KEY`, the setup and recovery keys and the first administrator's password. Depotex's stored settings can only be read with that encryption key: never run `init --force` on an installed instance, and back the key up with your database backups."),
            P("To keep secrets in Git (Sealed Secrets, SOPS or an external secret store), run `init --manifest`: it prints the Secret manifests instead of creating them."),

            H("First-boot setup"),
            TABLE(["`setup.mode`", "What happens"], [
                ["`auto` (default)", "Unattended setup once the licence is stored in the secret; the setup wizard until then"],
                ["`passive`", "Unattended setup from the values and the secrets"],
                ["`wizard`", "Open `<address>/setup?token=<setup key>` and fill it in (see [Getting Started](getting-started.html))"],
                ["`none`", "Already set up: no setup file, and the server no longer receives the setup key"],
            ]),

            H("Built-in or managed services"),
            TABLE(["Service", "Built in", "Managed instead"], [
                ["PostgreSQL", "`postgresql.enabled: true`: a database owned by a non-superuser role that may create the roles plugins need", "`postgresql.enabled: false` and `init --database-url 'postgres://…'` (RDS, Cloud SQL, Azure Database…)"],
                ["Redis", "`redis.enabled: true`: password set, admin commands disabled", "`redis.enabled: false` and `init --redis-url …`, or `--no-redis` for a single node"],
                ["Artifact storage", "`minio.enabled: true`: MinIO with the bucket and a user that can only use that bucket", "`storage.backend`: `s3`, `minio` (an external endpoint), `azure`, or `local` with a ReadWriteMany claim (`storage.local.existingClaim`) mounted on every server pod"],
            ]),
            P("The built-in services are single instances. For high availability use managed ones; `deploy/helm/depotex/values-external.yaml` is an example with managed PostgreSQL, Redis and S3, three server replicas and TLS."),

            H("Clustering"),
            UL([
                "The server runs as a StatefulSet: each pod keeps its name, because Depotex derives a server's identity, and the installation ID your licence is bound to, from it. Don't rename the release of an installed instance.",
                "More than one server replica (`backend.replicas`) is a cluster: it needs a Pro licence or higher, Redis, and shared storage. Start with one replica until setup has finished; pods start one after another. See [Single Node & Cluster](deployment-modes.html).",
                "The web app (`frontend.replicas`, 2 by default) is stateless.",
            ]),

            H("Network and security"),
            UL([
                "The ingress sends live updates (`/api/ws`) to the server and everything else to the web app, which forwards API and package-manager traffic. Set `ingress.className`, `ingress.tls` and your controller's annotations; for large uploads, raise its body size and timeouts (the values file shows the nginx annotations).",
                "Every pod runs as a non-root user with all capabilities dropped, a read-only root filesystem and no Kubernetes API token.",
                "Network policies (`networkPolicy.enabled`) let only the server reach PostgreSQL, Redis and MinIO, and only the ingress controller reach the apps. The server may reach the internet by default (upstream registries, single sign-on, email, webhooks); set `networkPolicy.backendInternetEgress: false` to allow only DNS, the built-in services and `extraEgress`.",
                "The web app never receives the setup or recovery key.",
                "With the ingress enabled the web app runs with `FRONTEND_BEHIND_PROXY=true`, so the client address the ingress controller sets reaches the server; the network policy keeps everything but the controller away from the web app. Behind a proxy of your own instead, set `frontend.env.FRONTEND_BEHIND_PROXY: \"true\"` only if that proxy sets the forwarded headers.",
            ]),

            H("Monitoring"),
            P("Set `backend.metrics.enabled: true` to expose each server pod's [Prometheus metrics](monitoring.html) on port 9090 (`backend.metrics.port`). The port is on the server's Service, never on the ingress, and the network policy lets Prometheus reach it: set `backend.metrics.prometheusNamespaceSelector` (for example `kubernetes.io/metadata.name: monitoring`) to allow only its namespace. With the Prometheus Operator, `backend.metrics.serviceMonitor.enabled: true` adds a ServiceMonitor (`interval`, `scrapeTimeout` and `labels` for your Prometheus's selector)."),
            CODE("""backend:
  metrics:
    enabled: true
    prometheusNamespaceSelector:
      kubernetes.io/metadata.name: monitoring
    serviceMonitor:
      enabled: true
      labels: { release: prometheus }"""),
            P("Rate limits and download quotas are shared by the server pods through Redis; tune them in **Settings → Security → Rate limits** or with `backend.env` (see [Rate limits](rate-limits.html#environment-variables)). Keep `backend.trustedProxies` covering the web app's and the ingress controller's pod addresses, or every visitor shares one address and one budget."),

            H("Test environment"),
            P("`values-dev.yaml` (with `init --dev`) adds MailHog to catch email, Keycloak with an OIDC and a SAML client, OpenLDAP with test users and groups, and a mock Okta, and `deploy/helm/scripts/dev-port-forward.sh` opens them on localhost."),
            WARN("Never use the test environment in production: it has test users, plain HTTP and relaxed security settings."),

            H("Backups"),
            P("The server stages each [backup](backups.html) in the pod's `/tmp` before writing it to storage. The chart gives `/tmp` 2 GiB: set `backend.tmpSize` larger than a compressed dump of your database plus the platform files, or point `BACKUP_TEMP_DIR` (in `backend.env`) at a larger volume. Back up the artifact storage itself with your storage platform's tools."),
            CODE("""backend:
  tmpSize: 20Gi"""),

            H("Upgrades"),
            P("Build and push the new images, then `helm upgrade` with the new tags. Server pods restart one at a time; database changes run once, on the first server to start."),
        ],
    )),
]
