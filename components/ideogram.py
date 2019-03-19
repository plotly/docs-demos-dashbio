import dash_bio as dashbio
import dash_html_components as html
import base64

component = dashbio.Ideogram(
  id='my-dashbio-ideogram',
  chrHeight=250
)

component_image = html.Img(
    src='data:image/png;base64,{}'.format(
        base64.b64encode(
            open(
                './images/pic_ideogram.png', 'rb'
            ).read()
        ).decode()
    )
)


def callbacks(app):
    return
