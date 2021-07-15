#Lesson6Task5

from random import randint

with open('numar.txt', 'w', encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f" Suma elementelor= {sum(my_list)}")
