import sqlite3
import crud 

db= sqlite3.connect('online_shop.db')

db.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL);
''')

db.execute('''CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE);
''')

db.execute('''CREATE TABLE IF NOT EXISTS orders ( 
           order_id INTEGER PRIMARY KEY, 
           customer_id INT NOT NULL, 
           product_id INTEGER NOT NULL, 
           quantity INTEGER NOT NULL, 
           order_date DATE NOT NULL, 
           FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
           FOREIGN KEY (product_id) REFERENCES products(product_id));
''')

'''
crud.add_product(db, "Mac", "laptop", 1500)
crud.add_product(db, "Legion", "laptop", 1000)
crud.add_product(db, "IPad", "tablet", 400)
crud.add_product(db, "Samsung", "tablet", 200)
crud.add_product(db, "HyperX Alloy FPS", "keyboard", 70)
crud.add_product(db, "ESport", "keyboard", 100)
crud.add_product(db, "Corsair", "keyboard", 180)
crud.add_product(db, "Logitec", "keyboard", 180)

crud.add_customer(db, "Mark", "Levyi", "mark@gmail.com")
crud.add_customer(db, "Pavel", "Pravyi", "pavel@gmail.com")
crud.add_customer(db, "Bob", "Dylan", "bob@gmail.com")
crud.add_customer(db, "Josh", "Maizer", "josh@gmail.com")
crud.add_customer(db, "Gregory", "Meinster", "gregory@gmail.com")

crud.make_order(db, 1, 1, 2)
crud.make_order(db, 2, 2, 1)
crud.make_order(db, 3, 3, 3)
crud.make_order(db, 4, 4, 4)
crud.make_order(db, 5, 5, 5)
crud.make_order(db, 1, 6, 6)
crud.make_order(db, 2, 7, 7)
crud.make_order(db, 3, 8, 8)
'''

while True:
    print('''
Що ви хочете зробити?

1 - Додавання продуктів:
2 - Додавання клієнтів:
3 - Замовлення товарів:
4 - Сумарний обсяг продажів:
5 - Кількість замовлень на кожного клієнта:
6 - Середній чек замовлення:
7 - Найбільш популярна категорія товарів:
8 - Загальна кількість товарів кожної категорії:
9 - Оновлення цін категорії на 10% більші:
10 - Показати усіх користувачів
11 - Показати усі продукти
12 - Показати усі замовлення(Joined)
0 - Вийти:

    ''')
    command = input("Оберіть ваші дії: ")

    if command == "1":
        product_name = input("Введіть назву продукту: ")
        category = input("Введіть категорію продукту: ")
        price = int(input("Введіть ціну продукту: "))
        crud.add_product(db, product_name, category, price)

    if command == "2":
        first_name = input("Введіть ім'я клієнта: ")
        last_name = input("Введіть прізвище клієнта: ")
        email = input("Введіть електронну пошту клієнта: ")
        crud.add_client(db, first_name, last_name, email)

    if command == "3":
        customer_id = input("Введіть id клієнта: ")
        product_id = int(input("Введіть id продукту: "))
        quantity = int(input("Введіть кількість товару: "))
        crud.make_order(db, customer_id, product_id, quantity)

    if command == "4":
        print(crud.get_total_income(db))

    if command == "5":
        print(crud.count_orders_by_customer_id(db))

    if command == "6":
        print(crud.average_check(db))

    if command == "7":
        pass

    if command == "8":
        pass

    if command == "9":
        pass

    if command == "10":
        pass

    if command == "11":
        pass

    if command == "12":
        pass

    if command == "0":
        pass