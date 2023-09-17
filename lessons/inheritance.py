class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"I am {self.firstname} {self.lastname}")


class Student(Person):
    pass


# Parent
pOne = Person("JC", "DC")
pOne.introduce()

# Student
sOne = Student("JC", "DC")
sOne.introduce()

#--override--#
class Persons:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"I am {self.firstname} {self.lastname}")


class Students(Persons):
    def __init__(self):
        pass

sOne = Students()

#--adding attributes--#
class PersonsAA:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"I am {self.firstname} {self.lastname}")


class StudentsAA(PersonsAA):
    def __init__(self, firstname, lastname, section):
        super().__init__(firstname, lastname)
        self.section = section
    
    def know(self):
        print(f"I am {self.firstname} {self.lastname} and I am from section {self.section}")

perOne = PersonsAA("j","c")
studOne = StudentsAA("j","c","2")
studOne.know()

#--overriding fucntions--#
class Persons1:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"I am {self.firstname} {self.lastname}")


class Students1(Persons1):
    def __init__(self, firstname, lastname, section):
        super().__init__(firstname, lastname)
        self.section = section
    
    def know(self):
        print(f"I am {self.firstname} {self.lastname} and I am from section {self.section}")

    def introduce(self):
        print(f"you are {self.firstname} {self.lastname}")


perOne1 = Persons1("j","c")
studOne1 = Students1("j","c","2")
perOne1.introduce()
studOne1.know()
studOne1.introduce()

#--customizing overrode functions--#
class Persons2:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"I am {self.firstname} {self.lastname}")


class Students2(Persons2):
    def __init__(self, firstname, lastname, section):
        super().__init__(firstname, lastname)
        self.section = section
    
    def know(self):
        print(f"I am {self.firstname} {self.lastname} and I am from section {self.section}")

    def introduce(self):
        super().introduce()
        print(f"you are {self.firstname} {self.lastname}")

perOne2 = Persons2("j","c")
studOne2 = Students2("j","c","2")
perOne2.introduce()
studOne2.know()
studOne2.introduce()