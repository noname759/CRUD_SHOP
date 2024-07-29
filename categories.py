import requests

API_URL = 'https://fakestoreapi.com'

def get_all_categories():
    url = f'{API_URL}/categories'
    response = requests.get(url)
    if response.status_code == 200:
        categories = response.json()
        return categories
    else:
        print("Не удалось получить список всех категорий.")
        return []

def get_products_of_category(category_name):
    url = f'{API_URL}/products/category/{category_name}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        print(f"Не удалось получить продукты для категории {category_name}.")
        return []
