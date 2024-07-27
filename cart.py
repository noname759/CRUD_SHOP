import requests
from pprint import pprint

def get_all_cart():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        carts = response.json()
        return carts

def get_single_cart(cart_id):
    response = requests.get(f'https://fakestoreapi.com/carts/{cart_id}')
    if response.status_code == 200:
        cart = response.json()
        return cart
    
def get_limit_carts(limit):
    response = requests.get(f'https://fakestoreapi.com/carts?limit={limit}')
    if response.status_code == 200:
        carts = response.json()
        return carts
    
def get_sorded_carts(sort_type):
    response = requests.get(f'https://fakestoreapi.com/carts?sort={sort_type}')
    if response.status_code == 200:
        carts = response.json()
        return carts


carts = get_sorded_carts('desc')
pprint(carts)