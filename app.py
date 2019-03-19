import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import os
# copy docs code here
        
component = ''
component_image = ''

# app code
app = dash.Dash()
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions']=True

for file_name in os.listdir('./components'):
    if file_name.endswith('.py') and 'app' not in file_name and 'config' not in file_name:
        exec('import components.{} as {}'.format(file_name.strip('.py'), file_name.strip('.py')))
        exec('{}.callbacks(app)'.format(file_name.strip('.py')))


server = app.server

# layout 
app.layout = html.Div(id='test', children=[
    dcc.Location(id='app-name', refresh=False),
    
    daq.ToggleSwitch(
        id='img-live',
        value=False,
        color='#ab63fa',
        style={'font-family': 'sans-serif',
               'font-variant': 'small-caps'},
        label=['image', 'live']
    ),
    html.Div(
        id='app-content', children=component_image
    ),
    html.Div(
        id='output'
    )
])


@app.callback(
    Output('app-content', 'children'),
    [Input('img-live', 'value'),
     Input('app-name', 'pathname')]
)
def change_img(show_live, app_name):
    component = ''
    component_image = ''
    if app_name is not None:
        app_name = app_name.strip('/')
        if len(app_name) > 0: 
            component = eval('{}.component'.format(app_name))
            component_image = eval('{}.component_image'.format(app_name))
    if show_live:
        return component
    return component_image


if __name__ == '__main__':
    app.run_server(debug=True)
