
def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 Not Found']


class Vega:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
