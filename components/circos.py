import dash_html_components as html
import dash_bio as dashbio
import urllib.request as urlreq
import base64
import json

# copy docs code here
data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/circos_graph_data.json").read().decode("utf-8")
circos_graph_data = json.loads(data)

component = html.Div(dashbio.Circos(
    id='my-dashbio-circos',
    layout=circos_graph_data['GRCh37'],
    tracks=[{
        'type': 'CHORDS',
        'data': circos_graph_data['chords'],
        'opacity': 0.7,
        'color': {'name': 'color'},
        'config': {
            'tooltipContent': {
                'source': 'source',
                'sourceID': 'id',
                'target': 'target',
                'targetID': 'id',
                'targetEnd': 'end'
            }
        }
    }]
), style={'transform': 'scale(0.5)',
          'width': '200vw',
          'margin-left': '-50vw',
          'margin-top': '-150px',
          'text-align': 'center'})

component_image = html.Div(html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_circos.png', 'rb'
            ).read()
        ).decode()
    )),
    style={'transform': 'scale(0.5)',
           'width': '200vw',
           'margin-left': '-50vw',
           'margin-top': '-151px',
           'text-align': 'center'}
)


def callbacks(app):
    return
