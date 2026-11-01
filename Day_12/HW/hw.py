user_num = int(input("Enter one number: "))

number = [1, 2, 3, 4, 5]

if user_num in number:
    print("Emtxveva")
else:
    print("Ar emTxveva")

print(number[0])
print(number[-1])
print(number[2])
for i in number:
    print(i)

grades = [48, 52, 69, 76, 84, 98]

more_than50 = 0
less_than50 = 0
for i in grades:
    print(i)

    if i >=50:
        more_than50+=1
    else:
        less_than50+=1

print(more_than50)
print(less_than50)

num = []
dadebiti=0
uaryofiti=0
nuli=0

for i in range(7):
    whole_num = int(input(f"Enter Whole number {i+1}: "))
    num.append(whole_num)

for i in num:
    if i>0:
        dadebiti+=1
    elif i <0:
        uaryofiti+=1
    else:
        nuli+=1

print("amdeni dadebitia",dadebiti)
print("amdeni uaryofitia",uaryofiti)
print("amdeni nulia",nuli)


yvelaze = num[0]

for u in num:
    if u > yvelaze:
        yvelaze=u
print(yvelaze)

movies = ["Iron man", "Spider man", "Superman" ]

for i in movies:
    print(i)
movie_in = input("Enter your movie name: ")
movies.append(movie_in)
for a in movies:
    print(a)

index = int(input("Enter index: "))
print(movies[index])