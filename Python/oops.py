# class bankaccount:
#     def __init__(self,account_number, name, balance = 0 ):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#        if amount <= 0:
#             print("Deposit amount must be positive.")
#             return
#        self.balance += amount
#        return self.balance
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#             return
#         if amount > self.balance:
#             print(f"Insufficient funds. Current balance: {self.balance}")
#             return
#         self.balance -= amount
#         return self.balance

#     def check_balance(self):
#         print(f"Account: {self.name} | Balance: {self.balance}")


# bank1 = bankaccount(202, "Sahil", 5000)
# bank1.deposit(3000)
# bank1.withdraw(8000)
# bank1.check_balance()






# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.reviews = []
        

#     def add_review(self, review):
#         self.reviews.append(review)
        
#     def count_reviews(self):
#         return len(self.reviews)

#     def display_reviews(self):
#         print(self.reviews)


# b1 = Book("Atomic Habits", "James Clear")

# b1.add_review("Very useful book")
# b1.add_review("Easy to understand")
# b1.add_review("Motivating")

# print("Title:", b1.title)
# print("Author:", b1.author)

# print("Total Reviews:", b1.count_reviews())

# b1.display_reviews()





# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.set_name(name)
#         self.set_roll_no(roll_no)
#         self.set_marks(marks)

#     def set_name(self, name):
#         if name.strip() != "":
#             self.__name = name
#         else:
#             print("Name cannot be empty.")
        
#     def get_name(self):
#         return self.__name()
    
#     def set_roll_no(self, roll_no):
#         if 1 <= roll_no<= 100:
#             self.__roll_no = roll_no
#         else:
#             print("Invalid roll number.")
    
#     def get_roll_no(self):
#         return self.__roll_no
    
#     def set_marks(self, marks):
#         if marks >= 0:
#             self.__marks = marks
    #         else:
    #             print("Marks cannot be negative.")
        
#     def get_marks(self):
#         return self.__marks
    

# stu1 = Student("vasu", 69, 80)

# print(stu1.get_name())
# print(stu1.get_roll_no())
# print(stu1.get_marks())





# class Shape:
#     def area(self):
#         print("Area")

# class circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r *self.r
        

# class Rectangle(Shape): 
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#     def area(self):
#         return self.lenght * self.width
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side


# # Objects
# c1 = circle(5)
# r1 = Rectangle(4, 6)
# s1 = Square(3)

# # Calling overridden methods
# print("Circle Area:", c1.area())
# print("Rectangle Area:", r1.area())
# print("Square Area:", s1.area())




# class Vehicle:
#     def  __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, sets):
#         super().__init__(brand, model)
#         self.sets = sets

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

# # Objects
# car1 = Car("Toyota", "Innova", 7)
# bike1 = Bike("Yamaha", "R15", 155)

# # Output
# print(car1.brand, car1.sets)
# print(bike1.brand, bike1.engine_cc)



# from abc import ABC, abstractmethod 
# class Employee:
#     @abstractmethod
#     def calculate_salary():
#         pass

# class Intern(Employee):
#     def __init__(self, stipend):
#         self.stipend = stipend

#     def calculate_salary(self):
#         return self.stipend
    
# class FullTimeEmployee(Employee):
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def calculate_salary(self):
#         return self.salary + self.bonus

# # Objects
# i1 = Intern(10000)
# f1 = FullTimeEmployee(50000, 10000)

# print("Intern Salary:", i1.calculate_salary())
# print("Full-Time Salary:", f1.calculate_salary())




# class Person:
#     def __init__(self, name, age = None, address = None):
#         self.name = name
#         self.age = age
#         self.address = address

#     def show(self):
#         print("Name", self.name)
#         print("age", self.age)
#         print("address", self.address)
#         print("--------------------")

# p1 = Person("Aryan")                         # name only
# p2 = Person("Vasu", 21)                      # name + age
# p3 = Person("Zoro", 22, "Mumbai")           # name + age + address


# # Output
# p1.show()
# p2.show()
# p3.show()




# class Player:
#     player_count = 0

#     def __init__(self, name, level):
#         self.name = name 
#         self.level = level
#         Player.player_count += 1

#     @classmethod
#     def show_player_count(cls):
#         print(f"The number of players is {Player.player_count}")

#     def show(self):
#         print("Name", self.name)
#         print("Level", self.level)
#         print("--------------------")

# # Creating players
# p1 = Player("Aryan", 5)
# p2 = Player("Vasu", 10)
# p3 = Player("Zoro", 7)

# # Display players
# p1.show()
# p2.show()
# p3.show()

# Player.show_player_count()
        




# Parent class 1
class Herbivore:
    def __init__(self):
        self.eats = "Plants"

    def herbivore_info(self):
        print("I eat plants only.")


# Parent class 2
class Carnivore:
    def __init__(self):
        self.hunts = True

    def carnivore_info(self):
        print("I eat meat and hunt other animals.")


# Child class (Multiple Inheritance)
class Bear(Herbivore, Carnivore):
    def __init__(self, name):
        self.name = name

        # Calling parent constructors manually
        Herbivore.__init__(self)
        Carnivore.__init__(self)

    def show_info(self):
        print("Name:", self.name)
        print("Eats:", self.eats)
        print("Hunts:", self.hunts)


# Object
b1 = Bear("Grizzly")

b1.show_info()
b1.herbivore_info()
b1.carnivore_info()