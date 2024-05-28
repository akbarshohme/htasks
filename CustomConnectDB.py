class Cars:
    def __init__(self, model, year, color, price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.model} ({self.year}) - {self.color} - ${self.price:,.2f}"

class CustomDB:
    def __init__(self):
        self.cars = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Committed")
        else:
            print("Rolled back")
        return True


with CustomDB() as db:
    db.cars.append(PorscheCar("911 Turbo S", 2023, "Guards Red", 218_000))
    db.cars.append(PorscheCar("911 GT3 RS", 2022, "Ultraviolet", 174_000))
    db.cars.append(PorscheCar("Taycan Turbo S", 2023, "Frozen Blue Metallic", 185_000))
    print("Porsche cars are in database: ")
    for car in db.cars:
        print(car)
