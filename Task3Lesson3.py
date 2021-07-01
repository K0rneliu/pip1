#Task3Lesson3

def my_funct(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    try:
        my_list.remove(min(my_list))
        return  sum(my_list)
    except TypeError:
        return "introduceti alt numar"
arg_1= int( input( "Intro1: "))
arg_2= int( input( "Intro1: "))
arg_3= int( input( "Intro1: "))
print(my_funct(arg_1, arg_2, arg_3))