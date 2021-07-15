#lesson5Task2


with open("L5t1.txt", encoding=' utf-8') as f:
    t_line = f.readlines()
    for numar, value in enumerate(t_line, 1):
        number_of_words = len(value.split())
        print(f'the string {numar} contains {number_of_words} words')