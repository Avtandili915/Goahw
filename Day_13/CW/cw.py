h = int(input("Enter number: "))

for i in range(h, 0, -1):
    
    for a in range(1, i + 1):
        print(a, end="")
print() 

h = int(input("Enter height: "))

for i in range(1, h + 1):
    print(" " * (h - i), end="")
    
    for j in range(1, i + 1):
        print(j, end="")
        
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

y = int(input("Enter number: "))

for l in range(1, y + 1):
    for p in range(1, l + 1):
       
        if p == 1 or p == l or l == y:
            print("*", end="")
        else:
            print(" ", end="")
        print()


n = 4 


for i in range(1, n + 1):

    dashoreba = " " * (n - i)
    varskvlavebi = "*" * (2 * i -1)
    print(dashoreba+varskvlavebi)