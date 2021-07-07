#task4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 3, 33, 2, 10, 29, 7, 4, 33, 29, 11]
new_list = [el for el in my_list if my_list.count(el) ==1]
print(f' {my_list}\n Unice: {new_list} ')

#var2
from random import randint

my_list1 = [randint(-10, 10) for _ in range (30)]
new_list1 = ([el for el in my_list1 if my_list1.count(el) ==1])
print(f'Sursa : {new_list1}\nValori unice:{new_list1}')
