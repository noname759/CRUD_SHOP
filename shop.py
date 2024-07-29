import requests
import categories
import products_api
import cart

def horizontall():
    print('------------------------')
    print('------------------------')
    print('------------------------')

while True: 
    horizontall()
    print('Добро пожаловать в наш магазин.')
    print('Наши категории: electronics | jewelery | men\'s clothing | women\'s clothing | ')
    print('###########################################')

    print('Выберите действия: ')
    print('1. Получить продукты выбранной категории.')
    print('2. Получить список всех товаров.')
    print('3. Получить список всех корзин.')
    print('4. Выход.')
    
    choose = input('Введите номер действия: ')
    
    if choose == '1':
        category = input('Введите категорию: ')
        products = categories.get_products_of_category(category)
        
        if products:
            for product in products:
                print(f'{product["id"]}. {product["title"]}. Цена: {product["price"]} $')
        else:
            print('Не удалось получить продукты для указанной категории или категория не существует.')

    elif choose == '2':
        products = products_api.get_all_products()
        
        if products:
            for product in products:
                print(f'{product["id"]}. {product["title"]}. Цена: {product["price"]} $')
        else:
            print('Не удалось получить список всех товаров.')

    elif choose == '3':
        carts = cart.get_all_cart()
        
        if carts:
            print('Список всех корзин:')
            for cart in carts:
                print(cart)
        else:
            print('Не удалось получить список всех корзин.')

    elif choose == '4':
        print('Выход из программы.')
        break

    else:
        print('Неверный выбор, пожалуйста, выберите снова.')
