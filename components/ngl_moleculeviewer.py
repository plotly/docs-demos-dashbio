from dash.dependencies import Input, Output
import dash_html_components as html
import urllib.request as urlreq
import base64
import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_bio_utils.ngl_parser as ngl_parser
import dash.exceptions as PreventUpdate

data_path = "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"

# PDB examples
dropdown_options = [
    {"label": "1BNA", "value": "1BNA"},
    {"label": "MPRO", "value": "MPRO"},
    {"label": "PLPR", "value": "PLPR"},
    {"label": "5L73", "value": "5L73"},
    {"label": "NSP2", "value": "NSP2"}
]

component = html.Div([
    dcc.Dropdown(
        id="default-dropdown",
        options=dropdown_options,
        placeholder="Select a molecule",
        value="1BNA"
    ),
    dashbio.NglMoleculeViewer(id="default-ngl")
], style={'transform': 'scale(0.8)'})

component_image = html.Div(html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_ngl_moleculeviewer.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '768px',
           'margin-left': '0px',
           'float': 'left'}
), style={'transform': 'scale(0.5)'})


def callbacks(app):
    @app.callback(
    Output("default-ngl", 'data'),
    Output("default-ngl", "molStyles"),
    Input("default-dropdown", "value")
    )
    def return_molecule(value):
        if (value is None):
            raise PreventUpdate

        molstyles_dict = {
            "representations": ["cartoon", "axes+box"],
            "chosenAtomsColor": "white",
            "chosenAtomsRadius": 1,
            "molSpacingXaxis": 100,
        }

        data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=value, color='red',
                                        reset_view=True, local=False)]

        return data_list, molstyles_dict
    return
