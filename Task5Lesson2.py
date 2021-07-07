# задача 1 урок 2


my_list=[1,5,6.9,'',"class",[3, 8], False, (3+1j), {"uno", 2, "barak"}]
for i, item in enumerate(my_list, 1):
    print(f"{i}. {type(item)} -- {item}")

    # задача 2 урок 2

    my_list = list(input("Enter nambers: "))
    print(len(my_list))

    for i in range(1, len(my_list), 2):
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

    print(my_list)

    import math
    import os




    # задача 3 урок 2

    nr_luna = int(input(" introduce-ti luna /de la 1 la 12/: "))
    while nr_luna > 12:
        nr_luna = int(input(" introduce-ti corect luna /de la 1 la 12/: "))
    if nr_luna < 3:
        print(f"Winter")
    elif nr_luna < 7:
        print(f"Spring")
    elif nr_luna < 7:
        print(f"Summer")
    elif nr_luna < 9:
        print(f"Autome")
    else:
        print(f"Winter")



 # задача 4 урок 2

my_list=input(" enter a string of several words separated by spaces: ").split()

for i, item in enumerate(my_list, 1):
    print(f'{i} {item[:10]}')

# задача 5 урок 2

my_list = [1, 3, 5, 7, 7, 9]
namb1 = int(input(" enter a natural number: "))

    print(f'{namb1}')
    i = 0
    for n in my_list:
        if namb1 >= n:
            i = i + 1
        else:
            break
    my_list.insert(i, namb1)
    print(my_list)

    from sys import argv

    print(argv)


