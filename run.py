from wsgiref.simple_server import make_server

from urls import routes, fronts
from vega_framework.main import Vega

app = Vega(routes, fronts)

with make_server('', 8000, app) as httpd:
    print('Serving on port 8000...')
    httpd.serve_forever()
