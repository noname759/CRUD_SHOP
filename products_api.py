import requests
from pprint import pprint

def get_all_products():
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
        return products

def get_single_product(product_id):
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    if response.status_code == 200:
        product = response.json()
        return product
    
def get_limit_products(limit):
    response = requests.get(f'https://fakestoreapi.com/products?limit={limit}')
    if response.status_code == 200:
        products = response.json()
        return products
    
def add_new_product(data):
    response = requests.post('https://fakestoreapi.com/products', data)
    if response.status_code == 200:
        new_product = response.json()
        return new_product
    
def edit_product(product_id, new_data):
    response = requests.patch(f'https://fakestoreapi.com/products/{product_id}', new_data)
    if response.status_code == 200:
        edited_product = response.json()
        return edited_product
    
def delete_product(product_id):
    response = requests.delete(f'https://fakestoreapi.com/products/{product_id}')
    if response.status_code == 200:
        return 'Продукт был успешно удалёен.'



input_list = int(input('Рақами id дохил кунед: '))
data = {
    
}

products = get_single_product(input_list)
pprint(products)