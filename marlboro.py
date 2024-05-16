from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

DB_PARAMS = {
    'dbname': 'ac_cback',
    'user': 'postgres',
    'password': 'miniqwerty',
    'host': 'localhost',
    'port': 5432
}

class Database:
    def __init__(self, params):
        try:
            self.conn = psycopg2.connect(**params)
            print("Database connection established.")
        except psycopg2.DatabaseError as e:
            print(f"Error connecting to the database: {e}")
            self.conn = None

    def execute_query(self, query, params=None, fetch=False):
        if self.conn is None:
            print("No database connection available.")
            return None
        try:
            with self.conn:
                with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query, params)
                    if fetch:
                        return cur.fetchall()
        except psycopg2.DatabaseError as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

class ProductRepository:
    @staticmethod
    def get_all_products(db):
        query = "SELECT * FROM products;"
        return db.execute_query(query, fetch=True)

    @staticmethod
    def save_product(db, product):
        query = """
        INSERT INTO products (name, image, is_liked, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (product.name, product.image, product.is_liked, product.created_at, product.updated_at)
        db.execute_query(query, params)

class UserRepository:
    @staticmethod
    def get_all_users(db):
        query = "SELECT * FROM users;"
        return db.execute_query(query, fetch=True)

    @staticmethod
    def save_user(db, user):
        query = "INSERT INTO users (username, email) VALUES (%s, %s);"
        params = (user.username, user.email)
        db.execute_query(query, params)

class Product:
    def __init__(self, name, image=None, is_liked=False, created_at=None, updated_at=None):
        self.name = name
        self.image = image
        self.is_liked = is_liked
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def save(self, db):
        ProductRepository.save_product(db, self)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self, db):
        UserRepository.save_user(db, self)
