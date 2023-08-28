num = 5
for x in range(0,num):
    for y in range(0,num-x-1):
        print(end=" ")
    for y in range(0,2*x+1):
        print("*",end="")
    print()
    
num = 1
for x in range(0,num):
    for y in range(0,num+1):
        print(end=" ")
    for y in range(0,1):
        print("*****",end=" ")
    print()
    
num = 3
for x in range(0,num):
    for y in range(0,num-1):
        print(end=" ")
    for y in range(0,1):
        print("*   *",end=" ")
    print()
    
num = 1
for x in range(0,num):
    for y in range(0,num+1):
        print(end=" ")
    for y in range(0,1):
        print("*****",end=" ")
    print()
    