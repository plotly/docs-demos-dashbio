import dash_html_components as html
import dash_bio as dashbio
import json
import urllib.request as urlreq
import base64

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/oncoprint_dataset3.json").read().decode("utf-8")
data = json.loads(data)

component = dashbio.OncoPrint(
    id='my-dashbio-oncoprint',
    data=data,
    width=800
)

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_oncoprint.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '800px', 'position': 'relative', 'top': '1px'}
)


def callbacks(app):
    return
