#Lesson5Task3

#my_file = open("H_R.txt", "w", encoding="utf-8")

#line = " "
#while line:
#   line = input("Input Name, salary: ")
#   my_file.write(f"{line}\n") if line != " " else my_file.close()

with open('H_R.txt', 'r', encoding='utf-8') as f:
    prim_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f' Salariu mediu = {round(sum(prim_dict.values())/ len(prim_dict), 2)}|n'
          f'Cu salarii mai mici de 20k{[e[0] for e in prim_dict.items() if e[1]<20000]}')

