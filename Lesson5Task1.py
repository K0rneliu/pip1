#Lesson5Task1


my_file = open("L5t1.txt", "w", encoding="utf-8")

line = " "
while line:
    line = input("introduceti cuvinte: ")
    my_file.write(f"{line}\n") if line != " " else my_file.close()


