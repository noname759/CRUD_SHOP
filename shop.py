import requests

API_URL = 'https://fakestoreapi.com'
cart = []

def print_main_menu():
    print("\nДобро пожаловать в наш магазин!")
    print('######################################')
    print("Категории: electronics, jewelery, men's clothing, women's clothing")
    print("Выберите действие:")
    print("1. Получить продукты по категории")
    print("2. Получить все товары")
    print("3. Показать корзину")
    print("4. Выход")

def get_products_by_category(category):
    url = f'{API_URL}/products/category/{category}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Не удалось получить продукты.")

def get_all_products():
    url = f'{API_URL}/products'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Не удалось получить все товары.")

def get_cart():
    if len(cart) == 0:
        print("Корзина пуста.")
    else:
        print("Ваша корзина:")
        for product_id in cart:
            url = f'{API_URL}/products/{product_id}'
            response = requests.get(url)
            if response.status_code == 200:
                product = response.json()
                print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
            else:
                print(f"Не удалось получить продукт с ID {product_id}.")

def add_to_cart(product_id):
    if product_id not in cart:
        cart.append(product_id)
        print(f"Товар с ID {product_id} добавлен в корзину.")
    else:
        print(f"Товар с ID {product_id} уже в корзине.")

def main():
    while True:
        print_main_menu()
        choice = input("Введите ваш выбор: ")

        if choice == '1':
            category = input("Введите категорию (electronics, jewelery, men's clothing, women's clothing): ").strip().lower()
            if category in ['electronics', 'jewelery', "men's clothing", "women's clothing"]:
                get_products_by_category(category)
            else:
                print("Неверная категория. Попробуйте снова.")
        elif choice == '2':
            get_all_products()
        elif choice == '3':
            get_cart()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()
