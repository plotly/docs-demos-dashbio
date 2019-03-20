import dash_html_components as html
import dash_core_components as dcc
import dash_bio as dashbio
import base64
import pandas as pd

# copy docs code here
df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv', sep='	', skiprows=4).set_index('model')
data = df.values

component = dcc.Graph(figure=dashbio.Clustergram(
    data=data,
    column_labels=list(df.columns.values),
    color_threshold={'row': 150, 'col': 700},
    row_labels=list(df.index),
    hide_labels=['row'],
    height=800,
    width=600
)[0])

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_clustergram.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '600px'}
)

def callbacks(app):
    return
