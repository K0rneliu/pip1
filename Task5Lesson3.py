#Task5Lesson3

def sum_num():
    s=0
    while True:
        my_list = input("introduceti un  numar sau 'q' pentru iesire").split()
        for num in my_list:
            if num == "q":
                return s
            else:
                try:
                    s+= int(num)
                except ValueError:
                    print("Pentru a iesi 'q'.")
        print((f"Suma numerilor = {s}"))


print(sum_num())