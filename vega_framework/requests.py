class GetRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for i in params:
                key, value = i.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequest.parse_input_data(query_string)
        return request_params


class PostRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for i in params:
                key, value = i.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(data_str)
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_input_data(data)
        return data
