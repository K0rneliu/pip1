#Task1Lesson3

def num_3(numb_1, numb_2):
    while numb_2 == 0:
        numb_2 = (int(input("Introduceti al doilea numar diferit de 0: ")))
    return round(numb_1 / numb_2, 2)
numb_1= (int(input("Introduceti primul numar: ")))
numb_2=- (int(input("Introduceti al doilea numar: ")))
print(num_3(numb_1, numb_2))