from database import DatabaseContextManager

#Table  = "Customer"
#Fields =[id, first_name, last_name, amount_spent]

#Table = "Product"
#Fields = [id, product_name, description, price]

#Table = "Orders"
#Fields = [id, date, customer_id, product_id]


def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                amount_spent FLOAT
                )"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)

def create_customer(first_name: str, last_name: str, amount_spent: int):
    query = """INSERT INTO Customer(first_name, last_name, amount_spent) VALUES(?,?,?)"""
    parameters = [first_name, last_name, amount_spent]
    with DatabaseContextManager("db2") as db:
        db.execute(query, parameters)

def update_customer(id :int, first_name:str, last_name:str, amount_spent:float):
    query = """UPDATE Customer
                SET first_name = ?, last_name = ?, amount_spent = ?
                WHERE id = ?"""
    parameters = [id, first_name, last_name, amount_spent]
    with DatabaseContextManager("db2") as db:
        db.execute(query, parameters)

def get_table_customer():
    query = """SELECT * FROM Customer"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("-------------------------------------------")

def drop_table_customer():
        query = """DROP TABLE Customer"""
        with DatabaseContextManager("db2") as db:
            db.execute(query)


def create_table_products():
    query = """CREATE TABLE Products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                description TEXT,
                price FLOAT
                )"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)

def create_product(product_name: str, description: str, price: float):
    query = """INSERT INTO Product(product_name, description, price) VALUES(?,?,?)"""
    parameters = [product_name, description, price]
    with DatabaseContextManager("db2") as db:
        db.execute(query, parameters)

def update_product(id :int, product_name:str, description:str, price:float):
    query = """UPDATE Product
                SET product_name = ?, description = ?, price = ?
                WHERE id = ?"""
    parameters = [id, product_name, description, price]
    with DatabaseContextManager("db2") as db:
        db.execute(query, parameters)

def get_table_product():
    query = """SELECT * FROM Product"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("-------------------------------------------")

def create_table_orders():
    query = """CREATE TABLE Orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE,
                customer_id INTEGER,
                product_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customer(id)
                FOREIGN KEY (product_id) REFERENCES Products(id)
                )"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)


#create_table_customer()
#create_customer("Antanas", "Antanaitis", 200)
#update_customer(id :int, first_name:str, last_name:str, amount_spent:float)
get_table_customer()
#drop_table_customer()


#create_table_products()
#create_product(product_name: str, description: str, price: float)
#update_product(id :int, product_name:str, description:str, price:float)
#get_table_products()

#create_table_orders()



