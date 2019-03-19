import dash_html_components as html
import dash_bio as dashbio
import urllib.request as urlreq
import base64


# copy docs code here

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_volcano.png', 'rb'
            ).read()
        ).decode()
    ),
    style={'width': '100%'}
)

component = ''


def callbacks(app):
    return 
