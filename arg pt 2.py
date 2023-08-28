# **kwargs
def printStudent(**student):
    print(student["name"])
    print(student["age"])


printStudent(name="JC", age=20)


def summationOf(*values):
    x = [value for value in values]
    return sum(x)


print(summationOf(1, 2, 3, 4, 33))

