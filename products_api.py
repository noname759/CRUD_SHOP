import requests
API_URL = 'https://fakestoreapi.com'

def get_all_products():
    url = f'{API_URL}/products'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f'{product["id"]}. {product["title"]}. Цена: {product["price"]}')
    else:
        print("Не удалось получить список всех продуктов.")

def get_products_of_category(category_name):
    url = f'{API_URL}/products/category/{category_name}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        print(f"Не удалось получить продукты для категории {category_name}.")
        return []
