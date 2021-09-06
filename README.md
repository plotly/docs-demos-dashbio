# docs-demos-dashbio

## About

This app is used in the [`dash_bio`](https://dash.plotly.com/dash-bio) docs as
examples of components that are slightly "heavier" and might cause the docs
page to load more slowly.

## Getting started

Start a virtual environment, activate it, and install the dependencies:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How the app works

The app contains a toggle switch. Upon visiting a sub-URL of this app
that corresponds to the name of a Dash Bio component, an image of that
component is displayed. When the toggle switch is changed over to
"live", a "live" version of the component is displayed and the user
can interact with it.

## Adding a new component
1. Add a picture of the component in `images/`
	* This image should be named `pic_{component name}.png`
2. Add a file in `components/`
Create a file `{component name}.py` in the
`components/` folder. This file should contain the following:
* The example code from the `dash_bio` docs (i.e., the code for the
  component that is found on [this
  page](https://dash.plot.ly/dash-bio)).
* A variable "component" that contains the component.
  * If it's a Python-based component:
   ```
  component = dcc.Graph(dash_bio.ComponentName(...))
  ```
    * If it's a React-based component:
   ```
    component = dash_bio.ComponentName(...)
  ```
* A variable "component_image" that contains an `html.Img` element
  that has a picture of the component.
* A function with the signature `def callbacks(app)`. If there are no
  callbacks required in the app, the function body should just be
  `return`. This function is here in case any of the components need a
  re-render for some reason (in this case, you can just use the
  `html.Div` element in the app with id `output` for the `Output`
  argument.
