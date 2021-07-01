#Task6Lesson3

def int_func():
    for word in input("introduceti cuvintele prin spatiu(cu majuscule):\n").split():
        litere = 0
        for litera in word:
            if 97<= ord(litera)<=122:
                litere +=1
        print(word.title() if litere == len(word) else f"{word} - numai litere minuscule!")


int_func()