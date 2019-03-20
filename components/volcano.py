import dash_html_components as html
import dash_core_components as dcc
import dash_bio as dashbio
import base64
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/volcano_data1.csv")
component = dcc.Graph(figure=dashbio.VolcanoPlot(
  dataframe=df
), style={'width': '800px'})

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_volcano.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '800px', 'position': 'relative', 'top': '1px'}
)


def callbacks(app):
    return
