# 1
def sayHello(name):
    print(f"Hello, {name}")


sayHello("JC")


# 2
def sayHello(name):
    print(f"Hello, {name}")


name1 = input("enter name: ")
sayHello(name1)


# 3
def sayHello(fname, sname):
    print(f"Hello, {fname} and {sname}")


name1 = input("enter fname: ")
name2 = input("enter sname: ")
sayHello(name1, name2)


# 4
def add(num1, num2):
    return num1 + num2


sum = add(5, 3)
print(sum)


# 5
def isLegalAge(num):
    if num >= 18:
        return True
    else:
        return False


print(isLegalAge(18))

#try
def square(num):
    return num ** 2

x= input("Input a number: ")
print("its square is "+ str(square(int(x))))

#args1
def sayHello(*names):
    for name in names:
        print("Hello, " + name)

sayHello("Claudio","Trisha","JC")

#args2-wrong
def sayHello(*names):
    print(f"Hello, {names}")

sayHello("Claudio","Trisha","JC")

#kwargs
def sayhellow(firstname, lastname):
    print(firstname + " "+lastname)

sayhellow(lastname= " dela Cruz", firstname= "Jhon Carlo")

#kwargs adv
def printFamily(*fname, lastname):
    for name in fname:
        print(name + " "+ lastname)

printFamily("Jhon Carlo", "Corazon", lastname="dela Cruz")



