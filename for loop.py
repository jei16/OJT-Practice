letters = ["a", "b", "c", "d", "e", " "]
for x in letters:
    print(x)

# else
letters = ["a", "b", "c", "d", "e"]
for x in letters:
    print(x)
else:
    print("done" + "\n")


# break
letters = ["a", "b", "c", "d", "e"]
for x in letters:
    print(x)
    if x == "c":
        print("c hahaha")
        break


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"Even number: {num}")
    else:
        print(f"Odd number: {num}")

# range
for x in range(21):
    print(x)

for y in range(3):
    print("Hello")

# AccountAuthentication
inputuser = input("Input Username: ")
inputpass = input("Input Password: ")
username = ["John", "Alenere", "David"]
password = ["abc123", "123abc", "hahatdog"]

for x in range(len(username)):
    if inputuser == username[x] and inputpass == password[x]:
        print(f"Hello, {username[x]}")
        break
    else:
        print("Account not found")
        break
