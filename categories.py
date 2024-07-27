import requests
from pprint import pprint

def get_all_categories():
    response = requests.get('https://fakestoreapi.com/products/categories')
    if response.status_code == 200:
        categories = response.json()
        return categories
    
def get_products_of_categorie(categorie_name):
    response = requests.get(f'https://fakestoreapi.com/products/category/{categorie_name}')
    if response.status_code == 200:
        categorie = response.json()
        return categorie

input_list = input('Гуруҳро муайян кунед: ')
categories = get_products_of_categorie(input_list)
pprint(categories)