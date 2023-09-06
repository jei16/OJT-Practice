class Character:
    def __init__(self):
        print("Hello")

hey = Character() 
hey1 = Character()

class Characters:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"{self.name} created")

x = Characters("Jc",100)
