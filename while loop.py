age = 12
while age < 19:
    print(age)
    age = age + 1
else:
    print(str(age) + " hello")


# accessing list
id = [1, 2, 3, 4, 5]
i = 0
while i <= 4:
    print(id[i])
    i = i + 1

id = [1, 2, 3, 4, 5]
i = 0
while i < len(id):
    print(id[i])
    i = i + 1

# for i in range (0,5):
# print(id[i])

while True:
    print("Hello world")
    break

# break
print("1 + 1?")
while True:
    answer = input("Enter your answer: ")
    if answer == "2":
        print("kurik")
        break
    else:
        print("Wrong! Try again!")

# conditional
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
while x < len(list):
    if list[x] % 2 == 0:
        print("Even number: " + str(list[x]))
    else:
        print("Odd number: " + str(list[x]))
    x = x + 1

# quiz
lives = int(input("input no of lives you want to have: "))

while lives > 0:
    x = input("5+5= ")
    if int(x) == 10:
        print("correct")
        break
    else:
        lives = lives - 1
        if lives > 1:
            print(f"try again, you have {lives} lives left!")
        elif lives == 1:
            print(f"try again, you have {lives} life left!")
        else:
            print(f"You lose! The correct answer is 10.")


