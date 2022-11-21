# from datetime import date
# class Contact:
#     def __init__(self, id_user, first_name, last_name, birth_date, profession):
#         self.id_user = id_user
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = birth_date
#         self.profession = profession

#     def get_information(self):
#         return f'ID: {self.id_user}\n First_name: {self.first_name}\n Last_name{self.last_name}\n Birth_date:{self.birth_date}\n Profession: {self.profession}'

# contact = Contact(1, 'Peskov', 'Nikolay', date(day = 12, month = 12, year = 1992), 'Python developer')
# print(contact.get_information())


# class Birds:
#     def __init__(self, view, age):
#         self.view = view
#         self.age = age

#     def eat(self):
#         return f"I eat worms"
    
#     def fly(self):
#         return f'I can fly'
    
#     def swim(self):
#         return f"I can't swim"
    
# class Mammals:
#     def __init__(self, view, age):
#         self.view = view
#         self.age = age

#     def eat(self):
#         return f"I eat grass"
    
#     def fly(self):
#         return f"I can't fly"
    
#     def swim(self):
#         return f"I can't swim"
    
# class Fishes:
#     def __init__(self, view, age):
#         self.view = view
#         self.age = age

#     def eat(self):
#         return f"I eat worms"
    
#     def fly(self):
#         return f"I can't fly"
    
#     def swim(self):
#         return f"I can swim"

# class Falcon(Birds):
#     def eat(self):
#         return f"I eat meat"
    
#     def fly(self):
#         return f"I can fly"
    
# class Pinguin(Birds):
#     def eat(self):
#         return f"I eat fish"
    
#     def fly(self):
#         return f"I can't fly"
    
#     def swim(self):
#         return f'I swim very well'
    
# class Trout(Fishes):
#     def eat(self):
#         return f'I eat shellfish'
    
#     def swim(self):
#         return f'I can swim'
    
# class Whale:
#     def eat(self):
#         return f"I eat krill"
    
#     def swim(self):
#         return f'I can swim'
    
# pinguin = Pinguin('royal', 12)
# print(pinguin.eat())
# print(pinguin.fly())
# print(pinguin.swim())

# falcon = Falcon('newtoni', 5)
# print(falcon.eat())
# print(falcon.fly())

# trout = Trout('trutta', 4)
# print(trout.eat())
# print(trout.swim())

# whale = Whale('blue', 7)
# print(whale.eat())
# print(whale.swim())


# def show_even_numbers(*args):
#     even_numbers_lst = []
#     for i in args:
#         try:
#             if i % 2 == 0:
#                 even_numbers_lst.append(i)

#         except TypeError:
#             continue 

#     return even_numbers_lst


# def vyvod(even_numbers_lst):
#     count = 1
#     for i in even_numbers_lst:
#         print(f'{count} - {i}')
#         count += 1

# vyvod(show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12))

