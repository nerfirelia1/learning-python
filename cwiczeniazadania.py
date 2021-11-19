def hello(name):
    print(f"Hello {name}")


name = "John"

hello("Jasiu")

print("Hello {}".format(name))

print("Hello " + name)


def awesome_func(x, y):
    return x**y


print(awesome_func(2, 4))

#------------------------------------------------cwiczenia z petlami ------------------------------

x=0
for x in range(0,4):
    print(x)