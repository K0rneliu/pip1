
# задача 5 урок 2

my_list= [1, 3, 5, 7, 7, 9]
namb1= int(input(" enter a natural number: "))
print(f'{namb1}')
i = 0
for n in my_list:
    if namb1 >= n:
        i =i + 1
    else:
        break
my_list.insert(i, namb1)
print(my_list)

















