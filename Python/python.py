# string = input("Enter a word: ")
# revers = string[::-1]
# if(string == revers):
#     print("This string is palindrom")
# else:
#     print("Its not a palindrom")


# nums = [2,2,2,2,2,2,2]
# sum = 0
# for i in nums:
#     sum = sum + i
# print(sum/len(nums))


# list1 = list(map(int,input("Enter values saprated by space: ").split()))
# list2 = list(map(int,input("Enter values saprated by space: ").split()))
# merged = list1 + list2
# merged.sort()
# print(merged)


# integers = (1,2,3,4,5,6,7,8,9,10,12,13,14,15,16)
# list_even = []
# list_odd = []

# for i in integers:
#     if (i%2 == 0):
#         list_even.append(i)
#     else:
#         list_odd.append(i)

# even = tuple(list_even)
# odd = tuple(list_odd)
# print(even)
# print(odd)


# students = { "Aryan" : 59, "Vasu" : 68, "Gagan" : 64,
#             "Anuj" :  81, "Avinash" : 89,}
# work = input("Enter A Add a student " "\n"
#             " Enter B Update marks " "\n"
#             "Enter C Search for a student" "\n"
#             "Enter D Display all students and marks").strip().upper()

# if (work == "A"): 
#     name = input("Enter name:").strip()
#     if(name in students):
#         print(f"{name} alredy exist.")
#     else:
#         number = int(input("Enter number: "))
#         students[name] = number 
#         print(f"{name} added successfully.")

# elif(work == "B"):
#     name = input("Enter name:").strip()
#     if(name not in students):
#         print(f"{name} does not exist.")
#     else:
#         number = int(input("Enter number: "))
#         students[name] = number 

# elif(work == "C"):
#     name = input("Enter studen name:")
#     if(name not in students):
#         print(f"{name} does not exist.")
#     else:
#         print(f"{name} → {students[name]} marks")
# else:
#     print(students.items())


# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# maps = {}
# for i in words:
#     maps[i] = len(i)
# print(maps)


# sentance = input("Enter a santance: ")
# space = sentance.count(" ")
# print(space)


# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8]

# set1 = set(list1)
# set2 = set(list2)
# check = set1.intersection(set2)
# if(len(check) == 0):
#     print("There are no common elements in the lists.")
# else:
#     print(f"The list shares {list(check)} common elements.")



# word = input("Enter a word:")
# print(set(word))
# print(sorted(set(word)))
# print(len(set(word)))



class product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        product.count+=1

    def get_info(self):
        print(f"The price of {self.name} is R.{self.price}.")

    @classmethod
    def get_count(cls):
        print(f"Total product in store = {cls.count}")

    @staticmethod
    def discount_price(price, discount):
        final_price = price - (price * discount/100)
        print(f"Discounted price = {final_price}")




p1 = product("phone", 20000)
p2 = product("laptop", 62000)
p3 = product("headphones", 2000)
product.get_count()