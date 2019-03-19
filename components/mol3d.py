import dash_html_components as html
import dash_bio as dashbio
import urllib.request as urlreq
import base64
import json
import urllib.request as urlreq


model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

component = dashbio.Molecule3dViewer(
  id='my-dashbio-molecule3dviewer',
  styles=styles_data,
  backgroundOpacity='0',
  modelData=model_data
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
