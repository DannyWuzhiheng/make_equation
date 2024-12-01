from resource import *
a=int(input("HOW MANY EQUATIONS YOU WANT?\n>"))
print(a)
for i in range(a):
    equation = generate_equation()
    print(equation)
