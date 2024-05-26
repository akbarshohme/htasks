import time
import sqlite3

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"It took {elapsed_time:.6f} seconds.")
        return False

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT * FROM my_table")
        print("Data before:")
        for row in self.cursor.fetchall():
            print(row)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.execute("UPDATE my_table SET value = value + 1 WHERE id = 1")
        self.connection.commit()

        self.cursor.execute("SELECT * FROM my_table")
        print("Data after:")
        for row in self.cursor.fetchall():
            print(row)

        self.cursor.close()
        self.connection.close()
        return False

with Timer() as timer:
    product = 1
    for i in range(1, 100001):
        product *= i
    print(f"Result: {product}")

with Database("n47_stuff.db") as db:
    pass
