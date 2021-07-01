# Task2Lesson3

def my_list(Name, Surname, Year_of_birth, City, Email, Phone):
    return f"{Name}; {Surname}; {Year_of_birth}; {City}; {Email}; {Phone}"

Name = input("Name: ")
Surname = input("Surname: ")
Year_of_birth = input("Yor year of birth: ")
City = input("Your city of residence: ")
Email = input("Your email: ")
Phone = input("Your number telefon: ")
print (my_list(Name, Surname, Year_of_birth, City, Email, Phone))