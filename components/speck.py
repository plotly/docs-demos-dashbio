from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bio as dashbio
import urllib.request as urlreq
import base64
import dash_bio.utils.xyz_reader as xyz_reader

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/speck_methane.xyz").read().decode("utf-8")
data = xyz_reader.read_xyz(data_string=data)

component = dashbio.Speck(
    data=data,
    id='speck',
    presetView='default',
    view={'resolution': 400},
    scrollZoom=True
)
component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_speck.png', 'rb'
            ).read()
        ).decode()
    ),
)


def callbacks(app):
    @app.callback(
        Output('output', 'children'),
        [Input('speck', 'view')]
    )
    def update(_):
        return ''
