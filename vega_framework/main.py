from quopri import decodestring

from vega_framework.requests import PostRequest, GetRequest


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


class Vega:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):

        # path
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'

        # request
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method
        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = Vega.decode_value(data)
            print(f'Пришел POST-запрос: {Vega.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = Vega.decode_value(request_params)
            print(f'Пришли GET-параметры: {Vega.decode_value(request_params)}')

        # page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound404()

        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data
