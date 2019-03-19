import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bio as dashbio
import dash_daq as daq
import urllib.request as urlreq
import base64
import json
import tempfile as tf
import dash_bio.utils.pdb_parser as parser
import dash_bio.utils.styles_parser as sparser

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/molecule3d_2mru.pdb").read().decode("utf-8")
tmp = tf.NamedTemporaryFile(suffix='.pdb', delete=False, mode='w+')
tmp.write(data)
fname = tmp.name
tmp.close()

model_data = json.loads(parser.create_data(fname))
styles_data = json.loads(sparser.create_style(fname, 'cartoon', 'chain'))


component = dashbio.Molecule3dViewer(
  id='my-dashbio-molecule3dviewer',
  modelData=model_data,
  styles=styles_data,
  backgroundOpacity='0'
)


component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_mol3d.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '500px', 'margin-left': 'calc(50% - 250px)'}
)


def callbacks(app):
    return
