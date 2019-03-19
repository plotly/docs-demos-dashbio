import dash_bio as dashbio
import dash_html_components as html
import dash_core_components as dcc
import base64
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/manhattan_data.csv")
component = dcc.Graph(figure=dashbio.ManhattanPlot(
    dataframe=df,
), style={'width': '700px'})

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_manhattan.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'margin-left': '1px'}
)


def callbacks(app):
    return
