import dash_html_components as html
import dash_bio as dashbio
import json
import urllib.request as urlreq
import base64

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/dash-needle-plot/data/PIK3CA.json").read()
mdata = json.loads(data)

component = dashbio.NeedlePlot(
  id='my-dashbio-needleplot',
  mutationData=mdata
)

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_needle_plot.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '700px'}
)


def callbacks(app):
    return
