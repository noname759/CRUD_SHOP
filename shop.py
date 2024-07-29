import requests

API_URL = 'https://fakestoreapi.com'
cart = []

def print_main_menu():
    """Печатает меню."""
    print("\nДобро пожаловать в наш магазин!")
    print("1. Продукты по категории")
    print("2. Все продукты")
    print("3. Корзина")
    print("4. Выход")

def get_products_by_category(category):
    """Показывает продукты по категории."""
    url = f'{API_URL}/products/category/{category}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Ошибка при получении продуктов.")

def get_all_products():
    """Показывает все продукты."""
    url = f'{API_URL}/products'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
    else:
        print("Ошибка при получении продуктов.")

def get_cart():
    """Показывает содержимое корзины."""
    if not cart:
        print("Корзина пуста.")
    else:
        for product_id in cart:
            url = f'{API_URL}/products/{product_id}'
            response = requests.get(url)
            if response.status_code == 200:
                product = response.json()
                print(f"ID: {product['id']}, Название: {product['title']}, Цена: ₽{product['price']}")
            else:
                print(f"Ошибка при получении товара с ID {product_id}.")

def add_to_cart(product_id):
    """Добавляет товар в корзину."""
    if product_id not in cart:
        cart.append(product_id)
        print(f"Товар с ID {product_id} добавлен в корзину.")
    else:
        print(f"Товар с ID {product_id} уже в корзине.")

def main():
    """Основная функция для выбора действий."""
    while True:
        print_main_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            category = input("Введите категорию: ").strip().lower()
            get_products_by_category(category)
        elif choice == '2':
            get_all_products()
        elif choice == '3':
            get_cart()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == '__main__':
    main()
