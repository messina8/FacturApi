import json

import requests
from random import random, randrange, choice, randint
from string import ascii_letters

import Sale
from Product import State
from Sale import Payment

suppliers = ['pla', 'sud', 'riv', 'vyr', None]
localhost = 'http://127.0.0.1:8000/'


def random_string():
    string = ''
    for a in range(randrange(3, 40)):
        string += choice(ascii_letters + ' ')
    return string


def random_products(qty=1):
    items = []
    for i in range(qty):
        item = {'title': random_string(), 'state': choice(list(State)), 'price': randrange(1000, 15000, 50)}
        if item['state'] == 'new':
            item['supplier'] = choice(suppliers)
        items.append(item)
    return items


def random_sales(qty=1):
    sales = []
    for i in range(qty):
        sale = {'products': random_products(randint(1, 8)), 'client_id': randint(1000000, 45000000),
                'payment_method': choice(list(Payment)), 'email': 'whatever@whatever.com'}
        total = 0
        for s in sale['products']:
            total += s['price']
        sale['total'] = total
        sales.append(sale)
    return sales


def post_sales(sales: list[Sale.Sale], url=localhost):
    for i in sales:
        requests.post(url + 'new_sale/', json.dumps(i))
