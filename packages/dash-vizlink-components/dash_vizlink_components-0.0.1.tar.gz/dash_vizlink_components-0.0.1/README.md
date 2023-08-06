# Dash Vizlink Components

Dash Vizlink Components is a Dash component library.

### Table of contents

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Installation

```bash
pip install dash
pip install dash-vizlink-components
```

## Quickstart

```python
import dash_vizlink_components as dvc
from dash import Dash, Input, Output, html

app = Dash(__name__)

app.layout = html.Div(
    [
        dvc.Breadcrumbs(
          id="breadcrumbs",
          items=[
            {'label': 'First'},
            {'label': 'Second'},
            {'label': 'Third'}
          ],
          value='Second'
        ),
        html.Div(id="content")
    ]
)


@app.callback(Output("content", "children"), Input("breadcrumbs", "value"))
def update_content(breadcrumb):
    return [
      html.H3(breadcrumb),
      html.P('This is the {} page.'.format(breadcrumb.lower()))
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
```

## Contributing

1. Install virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Install npm dependencies

    ```bash
    npm install
    ```

3. Add your new component in `src/lib/components`. Make sure to include it in the `src/lib/index.js` as well.

4. Build the components with the command: `npm run build`.

5. Raise a PR, including an example to reproduce the changes contributed by the PR.
