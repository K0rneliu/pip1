#Lesson6Task6

my_dict ={}
with open('Task6.txt', encoding="utf-8") as nob:
    for line in nob:
        nume, numar = line.split(' : ')
        name_sum = sum(map(int, "".join([i for i in numar if i == '' or '9' >= i >= '0']).split()))
        my_dict[nume] = name_sum
    print(f"{my_dict}")