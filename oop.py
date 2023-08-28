class Character:
    name = "Name"
    hp = 100
    mp =50
    atk =12
    lvl =1

characterX = Character()
characterY = Character()
characterX.name = "JC"
characterY.name = "DC"
characterX.mp = 123
print(characterX.name)
print(characterY.name)
print(characterX.mp)


hey=["a",'b','c']
hey.insert(1,"d")
print(hey)    

def my_function(*kids):
    print("hi" + " " + kids[1])

my_function("Emil","Lime","meil")


class Hello:
    def __init__(self):
        print("Hello World!")

charOne = Hello()