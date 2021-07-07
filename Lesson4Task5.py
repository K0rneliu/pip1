#task 5


from functools import reduce

def gen_list(el_1, el_2):
    return  el_1*el_2

pr_list = [el for el in range (100, 1001, 2)]
print( f"list\n{pr_list}\nGeneration\n{reduce(gen_list, pr_list)}")


#my_list = [num for num in range(30, 400, 10)]
#rez_list = [num * 3.9 if num %2 == 0 else num * 1 for num in my_list]
#rez_list1= [el if el>=100 or el<=1000 else el*0 for el in rez_list]

#print(rez_list1)