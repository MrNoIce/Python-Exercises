class Book:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page



mockingbird = Book()
mockingbird.title = "To Kill a Mockingbird"
mockingbird.publisher = "Penguin Books"
mockingbird.author = "Harper Lee"
mockingbird.year_published = 1960
mockingbird.publisher = "J. B. Lippincott & Co."

for prop, value in mockingbird.__dict__.items():
    print("book:",f'{prop}:\n{value}\n')


print(mockingbird.currently_reading)
mockingbird.start_reading()
print(mockingbird.currently_reading)
mockingbird.stop_reading(34)
mockingbird.start_reading()
mockingbird.stop_reading(89)
mockingbird.start_reading()



class Pizza:
    def __init__(self):
        self.size = 0
        self.type = ""
        self.toppings = ""
        self.ordered = False

    def add_topping(self,toppings):
        self.toppings = toppings

    def order_zah(self):
        self.ordered = True
        print(f"You ordered a {self.size} inch {self.type} pizza, with {self.toppings}")

pepperoni = Pizza()
pepperoni.size = 73
pepperoni.type = "Meat"
pepperoni.toppings = ("sausage", "pepperoni")
pepperoni.add_topping("onion",)
pepperoni.add_topping("olives",)
pepperoni.order_zah()

for prop, value in pepperoni.__dict__.items():
    print("Pizza:",f'{prop}:\n{value}\n')

