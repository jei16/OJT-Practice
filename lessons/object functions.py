class Animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice
    
    def speak(self):
        print(self.voice)

    def Introduce(self):
        print(f"I am a {self.type}")

aOne = Animal("Dog","Arf")
print(aOne.voice)
aOne.speak()


