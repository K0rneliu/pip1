# задача 3 урок 2


nr_luna = int(input(" introduce-ti luna /de la 1 la 12/: "))
while nr_luna > 12:
    nr_luna = int(input(" introduce-ti corect luna /de la 1 la 12/: "))
if nr_luna < 3:
    print(f"Winter")
elif nr_luna < 7:
    print(f"Spring")
elif nr_luna < 7:
    print(f"Summer")
elif nr_luna < 9:
    print(f"Autome")
else:
    print(f"Winter")