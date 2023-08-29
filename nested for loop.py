for x in range(5):
    for y in range(5):
        print("x")

# end
for x in range(5):
    for y in range(5):
        print("x", end="")
    print()

# multidimensional
courseStudents = [
    ["BSIT", "David"],
    ["BSIT", "Alenere"],
    ["BSCS", "Patrick"],
    ["BSCS", "Neymar"],
]
print(courseStudents[1][1])

for x in courseStudents:
    for y in x:
        print(y)
    print()

# data extract
students = [["BSIT", ["David", "Alenere"]], ["BSCS", ["Jaymar", "Emman", "Patrick"]]]

for w in students:
    print(w[0] + ":")
    for x in w[1]:
        print(" -" + x)
    print()
