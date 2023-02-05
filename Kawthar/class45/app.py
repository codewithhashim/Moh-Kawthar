# def func():
#     # code


class Cars:
    def __init__(self, automatic, doors):
        self.automatic = automatic
        self.doors = doors
        self.convertible = True
    
    def print_it (self):
        print(self.convertible)
        print(self.automatic)
        print(self.doors)
    
    def call_it(self):
        print(self.doors)


# audi =  Cars("Yes", 2)
# audi.print_it()
bugati = Cars("Yes", 4)
bugati.print_it()
bugati.call_it()



class Truck(Cars):
    def __init__(self, automatic, doors):
        super().__init__(automatic, doors)


gmc = Truck("Yes Truck", "6")
gmc.print_it()



# Books (class)

# Mystry (genre) books -> Object (self)

    # a person who created a car
    # a person who escaped the working loop 

# Fiction (genre) books -> books (self)

# crime genre is an instance of book class (self)


# inheritance