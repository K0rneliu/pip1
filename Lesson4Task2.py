#Task2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
sort_numb = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num-1]]
print(sort_numb)