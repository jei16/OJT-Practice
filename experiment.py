inputz = input("hellos: ")

x=len(inputz)
try:
    print(inputz[2:5])
except:
    print("None")

if x <5:
    print("i love you")
else:
    print("i hate you")


# Original string
text = "casadwdwdrlo"

# Define the variable xx that specifies the end index
xx = 4  # Replace with your desired end index

# Create a new string without the characters at indices 1 through xx
new_text = text[:1] + text[xx+1:]

# Print the new string
print(new_text)

xy = None

# Perform some computation or condition within a loop
for i in range(5):
    # Calculate a value based on the loop variable or other conditions
    print(i)  # For example, assign a value based on the loop variable i

# Now you can use the variable x outside the loop
print(xy)  

x = "ccccc"
print(len(str(x)) -2)

for i in range(6):
    print("x")