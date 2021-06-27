from django.shortcuts import render
from json import loads
import pathlib


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = from_json_load('products.json')
    return render(request, 'products/products.html', context)


def from_json_load(filename):
    filepath = pathlib.Path('products/fixtures/').joinpath(filename)
    try:
        data = loads(filepath.open(encoding='utf8').read())
        return data
    except IOError as error:
        print(error)

