import requests

API_URL = 'https://fakestoreapi.com'
cart = []

def print_main_menu():
    print("\nДобро пожаловать в наш магазин.")
    print('######################################')
    print("Наши категории: electronics / jewelery / men's clothing / women's clothing/")
    print("Выберите действия:")
    print("1. Получить продукты по выбранной категории")
    print("2. Получить список всех товаров")
    print("3. Получить список всех корзин")
    print("4. Выход")

def get_products_by_category(category):
    url = f'{API_URL}/products/category/{category}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f" {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Ошибка при получении продуктов.")

def get_all_products():
    url = f'{API_URL}/products'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f" {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Ошибка при получении всех продуктов.")

def get_cart():
    if not cart:
        print("Корзина пуста.")
    else:
        print("Ваша корзина:")
        for product_id in cart:
            url = f'{API_URL}/products/{product_id}'
            response = requests.get(url)
            if response.status_code == 200:
                product = response.json()
                print(f" {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
            else:
                print(f"Ошибка при получении продукта с ID {product_id}.")

def add_to_cart(product_id):
    global cart
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
            category = input("Введите категорию (electronics / jewelery / men's clothing / women's clothing): ").strip().lower()
            get_products_by_category(category)
            print('-------------------------------------------------')
            print('-------------------------------------------------')
            print('-------------------------------------------------')
        elif choice == '2':
            get_all_products()
            print('-------------------------------------------------')
            print('-------------------------------------------------')
            print('-------------------------------------------------')
        elif choice == '3':
            get_cart()
            print('-------------------------------------------------')
            print('-------------------------------------------------')
            print('-------------------------------------------------')
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")

if __name__ == '__main__':
    main()