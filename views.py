from vega_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', date=request.get('date', None))


class Registration:
    def __call__(self, request):
        return '200 OK', render('registration.html', date=request.get('date', None))
