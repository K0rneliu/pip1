#Task4Lesson3

def my_functi(x, y):
    try:
        x, y= float(x), int(y)
        if x <= 0 or y>=0:
            return "Respectati condditia: \nx si 0\ny"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f" x^y: {round(result, 2)}"
    except ValueError:
        return "necesar doar numere"


arg_1 =input ("Introduceti nr. pozitiv")
arg_2 =input( "Itroduceti nr. intreg negativ")

print((my_functi(arg_1, arg_2)))