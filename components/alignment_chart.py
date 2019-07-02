import dash_bio as dashbio
import six.moves.urllib.request as urlreq
import base64
import dash_html_components as html

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode("utf-8")

component = dashbio.AlignmentChart(
    id='my-dashbio-alignmentchart',
    data=data,
    width='500px'
)

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_alignment_chart.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '500px'}
)


def callbacks(app):
    return
