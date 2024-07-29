import requests
def get_all_cart():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        carts = response.json()
        return carts
    else:
        print("Не удалось получить данные о корзинах.")
        return []

def get_single_cart(cart_id):
    response = requests.get(f'https://fakestoreapi.com/carts/{cart_id}')
    if response.status_code == 200:
        cart = response.json()
        return cart
    else:
        print(f"Не удалось получить корзину с ID {cart_id}.")
        return {} 

def get_limit_carts(limit):
    response = requests.get(f'https://fakestoreapi.com/carts?limit={limit}')
    if response.status_code == 200:
        carts = response.json()
        return carts
    else:
        print(f"Не удалось получить корзины с лимитом {limit}.")
        return []

def get_sorted_carts(sort_type):
    response = requests.get(f'https://fakestoreapi.com/carts?sort={sort_type}')
    if response.status_code == 200:
        carts = response.json()
        return carts
        
    else:
        print(f"Не удалось получить отсортированные корзины по типу {sort_type}.")
        return []
carts = get_sorted_carts('desc')
