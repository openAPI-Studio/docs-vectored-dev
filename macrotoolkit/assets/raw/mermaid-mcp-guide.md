# Using the Mermaid Diagram Macro via MCP

## Overview

The Mermaid Diagram macro stores its configuration inline with the Confluence page content as macro parameters in the Confluence storage format (XHTML). To programmatically insert or update a Mermaid diagram via MCP, you need to write the correct storage format markup.

## Macro Config Schema

| Field       | Type   | Description                                            | Default |
|-------------|--------|--------------------------------------------------------|---------|
| code        | string | The Mermaid syntax source code                         | ''      |
| minHeight   | string | Container min-height: 'auto' or pixel value like '300' | 'auto'  |
| defaultZoom | string | Default zoom percentage: '50' to '200'                 | '100'   |

## Storage Format (XHTML)

When inserting via the Confluence REST API, the macro looks like this in storage format:

```xml
<ac:structured-macro ac:name="mermaid-diagram" ac:schema-version="1" ac:macro-id="unique-id">
  <ac:parameter ac:name="code">graph TD
  A[Start] --&gt; B{Decision}
  B --&gt;|Yes| C[Done]
  B --&gt;|No| D[Retry]</ac:parameter>
  <ac:parameter ac:name="minHeight">auto</ac:parameter>
  <ac:parameter ac:name="defaultZoom">100</ac:parameter>
</ac:structured-macro>
```

**Important:** HTML-encode special characters in the code parameter (`>` → `&gt;`, `<` → `&lt;`, `&` → `&amp;`).

## MCP Tool Definition

```json
{
  "name": "insert_mermaid_diagram",
  "description": "Insert a Mermaid diagram (flowchart, sequence, gantt, etc.) into a Confluence page",
  "inputSchema": {
    "type": "object",
    "properties": {
      "pageId": {
        "type": "string",
        "description": "The Confluence page ID to insert the diagram into"
      },
      "code": {
        "type": "string",
        "description": "Mermaid diagram syntax (e.g. 'graph TD\\n  A-->B')"
      },
      "minHeight": {
        "type": "string",
        "description": "Container min-height: 'auto' or pixel value",
        "default": "auto"
      },
      "defaultZoom": {
        "type": "string",
        "description": "Default zoom level: '50' to '200'",
        "default": "100"
      }
    },
    "required": ["pageId", "code"]
  }
}
```

## Implementation Pattern

```javascript
async function insertMermaidDiagram({ pageId, code, minHeight = 'auto', defaultZoom = '100' }) {
  // 1. Get current page content
  const page = await confluenceApi.get(`/wiki/api/v2/pages/${pageId}?body-format=storage`);

  // 2. HTML-encode the mermaid code for storage format
  const encodedCode = code
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

  // 3. Build the macro markup
  const macroMarkup = `
<ac:structured-macro ac:name="mermaid-diagram" ac:schema-version="1">
  <ac:parameter ac:name="code">${encodedCode}</ac:parameter>
  <ac:parameter ac:name="minHeight">${minHeight}</ac:parameter>
  <ac:parameter ac:name="defaultZoom">${defaultZoom}</ac:parameter>
</ac:structured-macro>`;

  // 4. Append to page body and update
  const newBody = page.body.storage.value + macroMarkup;

  await confluenceApi.put(`/wiki/api/v2/pages/${pageId}`, {
    version: { number: page.version.number + 1 },
    body: { storage: { value: newBody, representation: 'storage' } }
  });
}
```

## Supported Diagram Types for AI Generation

- `graph TD` / `graph LR` — Flowcharts
- `sequenceDiagram` — Sequence diagrams
- `classDiagram` — Class diagrams
- `stateDiagram-v2` — State machines
- `erDiagram` — Entity-relationship
- `gantt` — Gantt charts
- `pie` — Pie charts
- `gitGraph` — Git history
- `mindmap` — Mind maps
- `timeline` — Timelines

## Tips for MCP Integration

1. **Validate syntax** — Call `mermaid.parse(code)` server-side before saving to avoid broken diagrams
2. **Escape properly** — The code field goes into XML attributes, so encode `<`, `>`, `&`, `"`
3. **Newlines** — Use actual newlines in the code, not `\n` literals — storage format preserves them
4. **Update existing** — To update a diagram, find the `<ac:structured-macro ac:name="mermaid-diagram">` block in the page body and replace its code parameter
5. **App must be installed** — The macro only renders if the Forge app is installed on the Confluence site
