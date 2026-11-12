"""Admin guide: installing and running Depotex with its Helm chart, as a
runbook. The reference for images, network policies and monitoring stays on the
Docker & Kubernetes page (content_kubernetes.py). Keep in step with
deploy/helm in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

HELM = [
    ("helm-chart", dict(
        label="Install with Helm", title="Install with Helm", icon="server",
        desc="Install, license, scale, upgrade and remove Depotex on Kubernetes with its Helm chart, step by step",
        keywords=["helm", "chart", "kubernetes", "k8s", "values", "values.yaml", "prime-secrets", "install", "upgrade", "rollback", "uninstall", "statefulset", "ingress", "tls", "air-gapped", "openshift", "eks", "aks", "gke"],
        blocks=[
            NOTE("**Helm chart: TBD.** The address of the published chart repository and the public images will be announced here. Until then, use the chart (`deploy/helm/depotex`) and the `prime-secrets.sh` script from the Depotex distribution you received, and images built from it and pushed to your own registry. Ask [support](support.html) if you don't have them."),
            P("The chart deploys the Depotex server (a StatefulSet) and web app (a Deployment), with PostgreSQL, Redis and MinIO built in for a quick start, each of which can be switched off for a managed service. It never creates secrets: a script creates them beforehand and writes the installation's keys to a file you keep. This page walks through an installation from an empty namespace to a running, licensed cluster; [Docker & Kubernetes](kubernetes.html) is the reference for the images, network policies and monitoring."),

            H("Requirements"),
            TABLE(["", "Needed"], [
                ["Kubernetes", "1.27 or later, with a default StorageClass (or set `storageClass` per volume)"],
                ["Tools", "`kubectl` and Helm 3 on your workstation, with rights to create Secrets, StatefulSets, Services, Ingresses and NetworkPolicies in the namespace"],
                ["Ingress", "An ingress controller (ingress-nginx, Traefik, a cloud load balancer controller…) and a DNS name for Depotex; TLS from cert-manager or your own certificate"],
                ["Images", "The server and web app images in a registry your nodes can pull from (`backend.image`, `frontend.image`)"],
                ["License", "Requested once the installation ID is known (step 4); see [Licensing](licensing.html#get-a-license)"],
                ["For a cluster", "A Pro license or higher, Redis, and shared artifact storage (S3, MinIO, Azure or a ReadWriteMany volume)"],
            ]),
            P("Resource requests in the chart are a small starting point (server 250m CPU and 512 MiB, limit 2 GiB; web app 100m and 256 MiB, limit 1 GiB). See [Plan an installation](install-planning.html#sizing) before production."),

            H("1. Prepare values"),
            P("Start from one of these. Everything not set keeps the chart's default (the full list is under **Values reference** below)."),
            P("**Evaluation**: built-in PostgreSQL, Redis and MinIO, one server."),
            CODE("""# my-values.yaml
publicUrl: https://depotex.example.com
backend:
  image: { repository: registry.example.com/depotex/depotex-backend, tag: "<version>" }
frontend:
  image: { repository: registry.example.com/depotex/depotex-frontend, tag: "<version>" }
ingress:
  className: nginx
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
    cert-manager.io/cluster-issuer: letsencrypt
  tls: { enabled: true }"""),
            P("**Production**: managed PostgreSQL, Redis and S3, three servers (shipped as `values-external.yaml`)."),
            CODE("""publicUrl: https://depotex.example.com
backend:
  replicas: 3          # cluster mode: Pro license and Redis
  tmpSize: 40Gi        # scans plus room to stage backups
  resources:
    requests: { cpu: "2", memory: 4Gi }
    limits: { memory: 8Gi }
  metrics: { enabled: true, serviceMonitor: { enabled: true } }
postgresql: { enabled: false }
redis: { enabled: false }
minio: { enabled: false }
storage:
  backend: s3
  bucket: my-depotex-artifacts
  s3: { region: eu-west-1 }
ingress:
  className: nginx
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
  tls: { enabled: true, secretName: depotex-tls }
networkPolicy:
  ingressNamespaceSelector:
    kubernetes.io/metadata.name: ingress-nginx"""),
            P("**Air-gapped**: set `global.imageRegistry` to your mirror (prepended to every image, the built-in services' too) and `global.imagePullSecrets`. The server needs no internet access for itself; proxy repositories need their upstreams, which can be another Depotex (see [Upstreams](upstreams.html)). Set `networkPolicy.backendInternetEgress: false` and list what it may reach in `networkPolicy.extraEgress`."),

            H("2. Create the secrets"),
            CODE("""kubectl create namespace depotex
deploy/helm/prime-secrets.sh init -n depotex -r depotex \\
  --public-url https://depotex.example.com"""),
            P("The script generates every key and password, creates the Secrets `<release>-app` and `<release>-infra` in the namespace, and writes `depotex-<namespace>-<release>-install-keys.txt`, readable only by you. Options:"),
            TABLE(["Option", "Use"], [
                ["`-n`, `-r`", "Namespace and Helm release name (the release name is part of every resource name)"],
                ["`--public-url`", "The Depotex address, as in `publicUrl`"],
                ["`--database-url 'postgres://…'`", "A managed database instead of the built-in one; its role must own the database and have `CREATEROLE` (not superuser)"],
                ["`--redis-url 'rediss://…'` / `--no-redis`", "A managed Redis, or none (single server only)"],
                ["`--storage-access-key`, `--storage-secret-key`", "Credentials for S3, external MinIO or Azure (account name and key). Leave them out for S3 with an IAM role for the service account"],
                ["`--admin-password`", "Choose the first administrator's password instead of a generated one"],
                ["`--manifest`", "Print the Secret manifests instead of applying them: for Sealed Secrets, SOPS or an external secret store"],
                ["`--dev`", "Also the test tools' secret (MailHog, Keycloak, OpenLDAP); never in production"],
                ["`--force`", "Overwrite existing secrets. **Never on an installed instance**: a new `CONFIG_ENCRYPTION_KEY` makes every stored setting unreadable"],
            ]),
            WARN("Keep the keys file outside the cluster, with your database backups. It holds `CONFIG_ENCRYPTION_KEY`, the setup and recovery keys and the first administrator's password. Without the encryption key the installation can't start and its backups can't be restored."),

            H("3. Install"),
            CODE("""helm install depotex deploy/helm/depotex -n depotex -f my-values.yaml
kubectl -n depotex get pods -w"""),
            P("Pods wait in `CreateContainerConfigError` until the secrets exist. The server's init step waits for the built-in database. Without a license yet, the server starts in setup mode. `helm status depotex -n depotex` prints the next steps."),

            H("4. License it"),
            CODE("""deploy/helm/prime-secrets.sh installation-id -n depotex -r depotex
# request a license for that ID, then:
deploy/helm/prime-secrets.sh license license.json -n depotex -r depotex"""),
            P("The installation ID is printed and recorded in the keys file. Send it to Vectored through [vectored.dev/#contact](https://vectored.dev/#contact) or support@vectored.dev (see [Get a license](licensing.html#get-a-license)); the second command stores the license you receive in the app secret."),
            NOTE("The installation ID comes from the server pod's identity, which comes from the release name. Don't rename the release of an installed instance, and keep `fullnameOverride` unchanged once set."),

            H("First-boot setup"),
            TABLE(["`setup.mode`", "What happens"], [
                ["`auto` (default)", "Unattended setup as soon as the license is in the app secret; the setup wizard until then"],
                ["`passive`", "Unattended setup from the values and the secrets (fails until the license is there)"],
                ["`wizard`", "You open `<publicUrl>/setup?token=<SETUP_TOKEN>` and use the [setup wizard](setup-wizard.html)"],
                ["`none`", "Already set up: no setup file, and the server no longer receives the setup key"],
            ]),
            P("Unattended setup builds the [setup file](headless-setup.html) from the chart: the administrator from `setup.admin.email` and `setup.admin.name` with `ADMIN_PASSWORD` from the secret, the database, Redis and storage from the values and secrets."),
            CODE("""helm upgrade depotex deploy/helm/depotex -n depotex -f my-values.yaml
kubectl -n depotex logs -f depotex-backend-0"""),
            P("When the log shows the server running in normal mode, sign in at `publicUrl` as the administrator with the password from the keys file. Then set `setup.mode: none` in your values and upgrade once more, so the server stops receiving the setup key."),

            H("5. Check the installation"),
            UL([
                "`kubectl -n depotex get pods,pvc,ingress`: every pod `Running` and `Ready`, every claim `Bound`.",
                "Open **Settings → Advanced → System check** (Pro): database, Redis, storage, email, live updates and each server's health. A **Live updates** warning means the ingress isn't sending `/api/ws` to the server (the chart's ingress does this by default).",
                "Open the **?** menu → **About**: the version and which server answered.",
                "Push and pull one package through a test repository (see [Supported formats](formats.html)).",
            ]),

            H("Values reference"),
            TABLE(["Value", "Default", "Meaning"], [
                ["`publicUrl`", "`https://depotex.example.com`", "The address people open: redirects, single sign-on callbacks, email links, CORS, and the ingress host unless `ingress.host` is set"],
                ["`global.imageRegistry`", "empty", "Registry prepended to every image (air-gapped mirrors)"],
                ["`global.imagePullSecrets`", "`[]`", "Existing docker-registry secrets"],
                ["`nameOverride`, `fullnameOverride`", "empty", "Resource names; never change them on an installed instance"],
                ["`secrets.app`, `secrets.infra`, `secrets.dev`", "`<fullname>-app` …", "Names of the secrets `prime-secrets.sh` created, when you named them yourself"],
                ["`serviceAccount.create`, `.name`, `.annotations`", "`true`", "The pods' service account; annotate it for IAM roles (EKS IRSA, GKE Workload Identity)"],
                ["`setup.mode`", "`auto`", "`auto`, `passive`, `wizard` or `none` (above)"],
                ["`setup.admin.email`, `setup.admin.name`", "`admin@example.com`, `Administrator`", "The first administrator in unattended setup"],
                ["`setup.initImage.*`", "`busybox:1.37`", "Small image for the init steps (wait for the database, copy the setup file)"],
                ["`backend.image.*`", "`ghcr.io/openapi-studio/depotex-backend`, tag = chart `appVersion`", "Server image: `registry`, `repository`, `tag`, `digest`, `pullPolicy`"],
                ["`backend.replicas`", "`1`", "Servers. More than one is a cluster (Pro, Redis, shared storage). Keep 1 until setup has finished"],
                ["`backend.persistence.*`", "enabled, `ReadWriteOnce`, `10Gi`", "Per-pod data: bootstrap file, search index, this server's log files. Never artifacts"],
                ["`backend.tmpSize`", "`20Gi`", "The pod's `/tmp`, where backups are staged and images, packages and vulnerability data files are unpacked: larger than a compressed dump of your database, and than `IMAGE_SCAN_MAX_BYTES` + `IMAGE_SCAN_MAX_UNPACKED` (4 GiB + 16 GiB unless you set them in `backend.env`). The chart tells the server the limit (`TEMP_SPACE_LIMIT`) and requests the same ephemeral storage from the node"],
                ["`backend.scratch.enabled`, `backend.scratch.storageClass`, `backend.scratch.size`", "`false`, cluster default, `50Gi`", "Mount `/tmp` from a volume created and deleted with each pod instead of the node's disk, for images larger than your nodes can spare. `tmpSize` is not used then"],
                ["`backend.trustedProxies`", "loopback and private ranges", "Proxies whose `X-Forwarded-For` is trusted (`TRUSTED_PROXIES`); narrow it to your pod network"],
                ["`backend.logLevel`", "`info`", "`debug`, `info`, `warn` or `error`"],
                ["`backend.env`", "`{}`", "Any other [environment variable](environment-variables.html), as `NAME: value`"],
                ["`backend.resources`", "requests 250m / 512Mi, limit 2Gi", "Server resources"],
                ["`backend.nodeSelector`, `.tolerations`, `.affinity`, `.topologySpreadConstraints`, `.podAnnotations`", "empty", "Scheduling"],
                ["`backend.terminationGracePeriodSeconds`", "`45`", "Time to finish requests and jobs on shutdown"],
                ["`backend.pdb.*`", "enabled, `maxUnavailable: 1`", "PodDisruptionBudget"],
                ["`backend.metrics.enabled`, `.port`", "`false`, `9090`", "[Prometheus metrics](monitoring.html) on their own port, never through the ingress"],
                ["`backend.metrics.prometheusNamespaceSelector`", "`{}`", "Namespace labels allowed to scrape (empty: any namespace, that port only)"],
                ["`backend.metrics.serviceMonitor.*`", "disabled, `30s`, `10s`", "ServiceMonitor for the Prometheus Operator: `enabled`, `interval`, `scrapeTimeout`, `labels`"],
                ["`frontend.image.*`", "`ghcr.io/openapi-studio/depotex-frontend`", "Web app image"],
                ["`frontend.appDir`", "`apps/depotex/frontend`", "The app's directory inside the image"],
                ["`frontend.replicas`", "`2`", "Web app pods (stateless)"],
                ["`frontend.env`", "`{}`", "Web app variables, such as `FRONTEND_API_BODY_LIMIT` or `CSP_ENFORCE`"],
                ["`frontend.resources`, scheduling, `pdb`", "requests 100m / 256Mi, limit 1Gi", "As for the server"],
                ["`ingress.enabled`, `.className`, `.annotations`, `.host`", "enabled", "The ingress; the host comes from `publicUrl` unless set"],
                ["`ingress.tls.enabled`, `.secretName`", "`false`", "TLS at the ingress"],
                ["`ingress.backendPaths`", "`[/api/ws]`", "Paths sent straight to the server (live updates need WebSocket upgrades)"],
                ["`networkPolicy.enabled`", "`true`", "Only the server reaches PostgreSQL, Redis and MinIO; only the ingress controller reaches the apps"],
                ["`networkPolicy.ingressNamespaceSelector`", "`{}`", "Namespace labels of the ingress controller"],
                ["`networkPolicy.backendInternetEgress`", "`true`", "The server may reach the internet (upstream registries, single sign-on, email, webhooks). `false` allows DNS, the built-in services and `extraEgress` only"],
                ["`networkPolicy.extraEgress`", "`[]`", "Extra egress rules for the server"],
                ["`postgresql.enabled`", "`true`", "Built-in PostgreSQL 17 (single instance). `false` for a managed database (`--database-url`)"],
                ["`postgresql.persistence.size`, `.resources`, `.config`", "`20Gi`, 250m / 512Mi, `max_connections: 200`", "Built-in database sizing and `postgresql.conf` settings"],
                ["`redis.enabled`", "`true`", "Built-in Redis 7.4 (single instance). `false` for a managed Redis, or none for a single server"],
                ["`redis.maxmemory`, `.persistence.size`", "`256mb`, `2Gi`", "Built-in Redis sizing"],
                ["`storage.backend`", "`minio`", "`minio`, `s3`, `azure` or `local`"],
                ["`storage.bucket`", "`depotex`", "Bucket (S3, MinIO)"],
                ["`storage.minio.endpoint`, `.useSSL`", "empty (built-in), `false`", "An external MinIO"],
                ["`storage.s3.region`", "`us-east-1`", "S3 region"],
                ["`storage.azure.container`", "`depotex`", "Azure container; the access key is the account name, the secret key the account key"],
                ["`storage.local.existingClaim`, `.path`", "empty, `/app/storage`", "A ReadWriteMany claim mounted on every server pod"],
                ["`minio.enabled`, `.persistence.size`", "`true`, `100Gi`", "Built-in MinIO (single instance) with the bucket and a user limited to it"],
                ["`dev.*`", "disabled", "Test tools (MailHog, Keycloak, OpenLDAP, a mock Okta) from `values-dev.yaml`. Never in production"],
            ]),

            H("Scale to a cluster"),
            STEPS([
                "Check the license|Pro or higher, with enough servers (Settings → Application → Licensing).",
                "Use Redis and shared storage|Built-in or managed Redis, and S3, MinIO, Azure or a ReadWriteMany volume. Local disk per pod doesn't work for a cluster.",
                "Size the database|Each server opens up to `pool_max_conns` connections: keep servers × `pool_max_conns` under PostgreSQL's `max_connections`. See [Database connections](deployment-modes.html#database-connections).",
                "Scale|Set `backend.replicas` and `helm upgrade`. Pods start one after another and join the cluster; **Settings → Clustering** lists them.",
            ]),
            P("Scaling down: lower `backend.replicas`. A removed pod shuts down cleanly and shows as **left**; it drops off the list after a day."),

            H("Upgrade"),
            STEPS([
                "Read the release notes|The [changelog](changelog.html) and [security advisories](security-advisories.html).",
                "Back up|Run a backup in **Settings → Backups** and check it finished.",
                "Upgrade|Push the new images, set their tags, and `helm upgrade depotex deploy/helm/depotex -n depotex -f my-values.yaml`.",
                "Watch|`kubectl -n depotex rollout status statefulset/depotex-backend`. Server pods restart one at a time; database migrations run once, on the first new server, while the others keep serving.",
                "Check|System check, the About dialog's version, and a test download.",
            ]),
            P("See [Upgrades & maintenance](upgrades.html) for what happens during a rolling upgrade and how to roll back."),

            H("Uninstall"),
            CODE("""helm uninstall depotex -n depotex"""),
            UL([
                "Removes the pods, services and ingress. The server pods' PersistentVolumeClaims, the built-in services' volumes and the secrets `prime-secrets.sh` created **are kept**: delete them yourself when you mean to throw the installation away (`kubectl -n depotex delete pvc,secret -l app.kubernetes.io/instance=depotex`, after checking what that selects).",
                "Artifacts in external storage (S3, Azure, an external MinIO) are never touched.",
                "Re-installing with the same release name and the kept secrets and volumes brings the same installation back.",
            ]),

            H("Troubleshooting"),
            TABLE(["Symptom", "Cause and fix"], [
                ["Pods in `CreateContainerConfigError`", "The secrets don't exist yet, or have other names: run `prime-secrets.sh init` with the same `-n` and `-r`, or set `secrets.app` / `secrets.infra`"],
                ["Server pod waiting in its init step", "The built-in PostgreSQL isn't ready (check its pod and PVC), or a managed database isn't reachable through the network policy"],
                ["Pod `Pending`", "A PersistentVolumeClaim can't be bound: no default StorageClass, or the size isn't available"],
                ["Setup doesn't start on its own", "`setup.mode: auto` waits for the license in the app secret: run `prime-secrets.sh license …`, then `helm upgrade`"],
                ["`413` on large uploads", "The ingress limits request bodies: `nginx.ingress.kubernetes.io/proxy-body-size: \"0\"` (or your controller's equivalent)"],
                ["Large downloads or uploads cut off", "Raise the ingress read and send timeouts (3600 s in the examples)"],
                ["Alerts arrive late; system check warns about live updates", "`/api/ws` doesn't reach the server with WebSocket upgrades: keep it in `ingress.backendPaths`, and allow upgrades on any proxy in front"],
                ["Everyone shares one rate limit or address in the audit log", "`backend.trustedProxies` doesn't cover the web app's and ingress controller's pod addresses"],
                ["Every page answers `402 license_required`", "The license expired or was issued for another installation ID: see [Licensing](licensing.html#when-a-license-expires)"],
                ["The server starts in recovery mode", "Something it needs is wrong (database, encryption key, storage, Redis, license): open the recovery link from its log, see [Recovery Mode](recovery.html)"],
            ]),
            P("Still stuck? Collect the details in [Support](support.html#what-to-send) and contact us."),
        ])),
]
