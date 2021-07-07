#lesson4Task7



def fact_gen(number):
    f_num = 1
    for i in range(number +1):
        yield f"{i}! = {f_num}"
        f_num *= i+1


for el in fact_gen(int(input("Numar factorial: "))):
    print(el)

#varianta2

from functools import reduce


def fact(n):
    try:
        yield reduce(lambda x, y: x*y, list(el if el > 0 else 1 for el in range(n+1)))
    except TypeError:
        yield  0


for i in fact((int(input("Numar factorial: ")))):
    print(i)
