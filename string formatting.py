from datetime import datetime
from string import Template

name = "Pete"
print("Hello %s" % name)


num = 5
print("I have %d apples" % num)

name = "John"
age = 20
print("Hello I'm {}, my age is {}".format(name, age))
print("Hello I'm {0}, my age is {1}".format(name, age))
print("Hello I'm {1}, my age is {0}".format(name, age))

a = 5
b = 10
print(f"Five plus ten is {a + b} and not {2 * (a + b)}.")


name = "Robert"
messages = 12
print(f"Hi, {name}. " f"You have {messages} unread messages")

now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
print(f"date and time: {now=}")


name1 = "jj"
print(f"{name1.upper() = :─^20}")
print(f"{name1.upper() = :^20}")
print(f"{name1.upper() = :20}")

a = 10000000
print("1." + " " + f"{a:,}")

b = 3.1415926
print(f"{b:.2f}")

c = 0.816562
print(f"{c:.2%}")

name3 = "eli"
t = Template("Hey $name2!")
print(t.substitute(name2=name3))
