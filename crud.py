import sqlite3

def add_product(db, product_name: str, category:str, price:int):
        db.execute('''INSERT INTO products(product_name, category, price)
                   VALUES(?,?,?)''', (product_name, category, price))
        db.commit()

def add_customer(db, first_name: str, last_name:str, email:str):
        db.execute('''INSERT INTO customers(first_name, last_name, email)
                   VALUES(?,?,?)''', (first_name, last_name, email))
        db.commit()

def make_order(db, customer_id: int, product_id: int, quantity: int):
    db.execute('''INSERT INTO orders (customer_id, product_id, quantity, order_date)
               VALUES(?, ?, ?, CURRENT_TIMESTAMP)''', (customer_id, product_id, quantity))
    db.commit()

def get_total_income(db):
       r = db.execute('''SELECT SUM(products.price*order.quantity) AS total_price
                FROM orders
                INNER JOIN products ON orders.product_id = products.product_id
                ''')
       return r.fetchone()

def count_orders_by_customer_id(db):
        r = db.execute('''SELECT customers.first_name AS customer_name, COUNT (orders.order_id) AS amount_of_orders
                FROM orders
                INNER JOIN customers ON orders.customer_id = customers.customer_id
                GROUP BY customers.first_name 
                ORDER BY customers.customer_id ASC
                ''')
        return r.fetchall()

def average_check(db):
        r = db.execute('''SELECT AVG(products.price*order.quantity) AS average_price
                FROM orders
                INNER JOIN products ON orders.product_id = products.product_id
                ''')
        return r.fetchone()