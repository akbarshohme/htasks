# 1-answer
#
# import psycopg2
#
# db_connection = psycopg2.connect(
#     host='localhost',
#     database_name='postgres',
#     user_name='postgres',
#     port_number=5432,
#     user_password='miniqwerty'
# )
#
# database_cursor = db_connection.cursor()
#
#
# 2-answer
#
# def add_product(name, price):
#     query = "INSERT INTO items (name, price) VALUES (%s, %s)"
#     values = (name, price)
#     db_cursor.execute(query, values)
#     db_connection.commit()
#
# def get_all_products():
#     query = "SELECT * FROM items"
#     db_cursor.execute(query)
#     products = db_cursor.fetchall()
#     return products
#
# def update_product(item_id, new_name, new_price):
#     query = "UPDATE items SET name = %s, price = %s WHERE id = %s"
#     values = (new_name, new_price, item_id)
#     db_cursor.execute(query, values)
#     db_connection.commit()
#
# def delete_product(item_id):
#     query = "DELETE FROM items WHERE id = %s"
#     values = (item_id,)
#     db_cursor.execute(query, values)
#     db_connection.commit()
#
#
# 3-answer
#
# class Alphabet:
#     def __init__(self):
#         self.current_index = 0
#         self.alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index < len(self.alphabet):
#             current_letter = self.alphabet[self.current_index]
#             self.current_index += 1
#             return current_letter
#         else:
#             raise StopIteration
#
#
# 4-answer
#
# import time
# import threading
#
# def print_numbers():
#     for num in range(1, 6):
#         print(num)
#
# def print_letters():
#     letters = ['A', 'B', 'C', 'D', 'E']
#     for letter in letters:
#         print(letter)
#         time.sleep(1)
#
# thread1 = threading.Thread(target=print_letters)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# 5-answer
#
# class Product:
#     def __init__(self, name, price, item_id=None):
#         self.name = name
#         self.price = price
#         self.item_id = item_id
#
#     def save(self):
#         if self.item_id is None:
#             add_product(self.name, self.price)
#         else:
#             update_product(self.item_id, self.name, self.price)
#
#
# 6-answer
#
# class DbConnection:
#     def __init__(self, database_name, user, password, host='localhost', port='5432'):
#         self.database_name = database_name
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#         self.connection = None
#         self.cursor = None
#         self.connected = False
#
#     def connect(self):
#         try:
#             self.connection = psycopg2.connect(
#                 database=self.database_name,
#                 user=self.user,
#                 password=self.password,
#                 host=self.host,
#                 port=self.port
#             )
#             self.cursor = self.connection.cursor()
#             self.connected = True
#             print("Connected to database")
#         except psycopg2.OperationalError as e:
#             print(f"Error: {e}")
#             print("Attempting to reconnect...")
#             time.sleep(2)
#             self.connect()
#
#     def disconnect(self):
#         try:
#             if self.cursor:
#                 self.cursor.close()
#             if self.connection:
#                 self.connection.close()
#                 self.connected = False
#                 print("Disconnected from database")
#         except Exception as e:
#             print(f"Error: {e}")
#
#     def execute(self, query):
#         if not self.connected:
#             print("Attempting to reconnect...")
#             self.connect()
#         try:
#             self.cursor.execute(query)
#             print("Query executed")
#         except Exception as e:
#             print(f"Error {e}")
#
#     def __enter__(self):
#         self.connect()
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.disconnect()
#
#
# 7-answer
#
# class DbConnection:
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             host='localhost',
#             dbname='postgres',
#             user='postgres',
#             password='miniqwerty',
#             port=5432
#         )
#         return self.conn.cursor()
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.conn.commit()
#         self.conn.close()
#
# class Product:
#     def __init__(self, name, price, item_id=None):
#         self.name = name
#         self.price = price
#         self.item_id = item_id
#
#     def save(self):
#         with DbConnection() as cur:
#             if self.item_id is None:
#                 cur.execute("INSERT INTO Product (name, price) VALUES (%s, %s) RETURNING id", (self.name, self.price))
#                 self.item_id = cur.fetchone()[0]
#             else:
#                 cur.execute("UPDATE Product SET name = %s, price = %s WHERE id = %s", (self.name, self.price, self.item_id))
#
# def save_data_from_url_to_database(url):
#     response = requests.get(url)
#     data = response.json()
#     for product_data in data['products']:
#         product = Product(product_data['name'], product_data['price'])
#         product.save()
#     print("Data saved successfully.")
#
# url = "https://dummyjson.com/products/"
# save_data_from_url_to_database(url)
# 
#
