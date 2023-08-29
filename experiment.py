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