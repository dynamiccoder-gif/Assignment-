class product:
    def __init__(self, pid, manufacture_location):
        self.__pid = pid
        self.__manufacture = manufacture_location
    
    def get_pid(self):
        return self.__pid
    def get_manufacture(self):
        return self.__manufacture
    
    def set_pid(self, pid):
        self.__pid = pid
    def set_manufacture(self, update_m):
        self.__manufacture = update_m

    def __str__(self):
        return f"PID = {self.__pid} and manufacture_location = {self.__manufacture}"
    
    def print_data(self):
        print(self.__str__())

class Book(product):
    def __init__(self, pid, manufacture_location, name, pages, author, price):
        super().__init__(pid, manufacture_location)
        self.__name = name
        self.__number_of_pages = pages
        self.__author = author
        self.__price = price
    
   
    def get_author(self): return self.__author
    def get_name(self): return self.__name
    def get_pages(self): return self.__number_of_pages
    def get_price(self): return self.__price
    
    
    def set_author(self, author):
        self.__author = author
    def set_pages(self, page):
        self.__number_of_pages = page
    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, Book: {self.__name}, Author: {self.__author}, Pages: {self.__number_of_pages}, Price: {self.__price}"

    def print_data_book(self):
        print(self.__str__())

    def valid_data(self):
        if self.__price <= 0:
            print(f"Price '{self.__price}' is not valid.")
        else:
            print(f"Valid price: {self.__price}")




my_book = Book("rx47", "Agra", "half girlfreind", 400, "Chetan Bhagat", 500)
my_book.print_data_book()


my_book.valid_data()


bad_price_book = Book("rx100", "Delhi", "book1", 100, "pabelo", 0)
bad_price_book.valid_data()
print(my_book.get_author())
print(my_book.get_manufacture())
print(my_book.get_price())