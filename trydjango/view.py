from django.http import HttpResponse
import random

def home_view(Request):
    name = 'raulgane'
    number = random.random(10, 1000)
    HTML_STRING = f'<h1>Hello friends I am {name} and this is my {number} time!</h1>'

    return HttpResponse(HTML_STRING)