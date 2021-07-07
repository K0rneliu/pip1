# задача 4 урок 2


my_list=input(" enter a string of several words separated by spaces: ").split()

for i, item in enumerate(my_list, 1):
    print(f'{i} {item[:10]}')