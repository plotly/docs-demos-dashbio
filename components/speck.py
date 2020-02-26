from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bio as dashbio
import urllib.request as urlreq
import base64
import dash_bio_utils.xyz_reader as xyz_reader

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/dash-speck/data/methane.xyz").read().decode("utf-8")
data = xyz_reader.read_xyz(data, is_datafile=False)

component = html.Div(dashbio.Speck(
    data=data,
    id='speck',
    presetView='default',
    scrollZoom=True
), style={'transform': 'scale(0.5)',
          'margin-top': '-190px'})

component_image = html.Div(html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_speck.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '768px',
           'margin-left': '0px',
           'float': 'left'}
), style={'transform': 'scale(0.5)'})

def callbacks(app):
    return
