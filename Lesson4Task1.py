#Lesson4task1

from sys import argv


def calc_salary():
    try:
        time, rate, prima = map(float, argv[1:])
        print(f"salary: {time*rate+prima}")
    except ValueError:
        print("enter time, rata , prima")


calc_salary()