#leson4Task5

from from intertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el+1)]
        r_list = inter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return  repeat_list
    except ValueError:
        return "Eroare"
    except TypeError:
        return "TypeError"


print((unexpected(input("Start: "), input("Pana la "), input("nr repetari -"))))
