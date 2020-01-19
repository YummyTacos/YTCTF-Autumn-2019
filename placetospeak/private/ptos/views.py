from django.shortcuts import render


def handler_error(code, text):
    return lambda request, exception=None: render(request, 'error.html', {'code': code, 'text': text}, status=code)
