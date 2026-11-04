# # 1) შექმენით რიცხვების მასივი (მინიმუმ 20 რიცხვი), თქვენი დავალებაა for ციკლის დახმარებით გადაუაროთ მასივს და თითოეული რიცხვი რომელიც მდებარეობს ამ მასივში აიყვანოთ კვადრატში და შედეგე (ანუ ყველა კვადრატში აყვანილი რიცხვი) უნდა დააჯმამოთ.

# # 2) იმავე მასივს გადაუარეთ for ციკლის დახმარებით, თქვენი დავალებაა კენტი რიცხვები ცალკე დააჯამოთ და ლუწი რიცხვები ცალკე, საბოლოოდ გამოიტანეთ ლუწი და კენტი რიცხვების ჯამები ტერმინალში.


# # numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # sum = 0
# # for i in numbers:
# #     sum+=i**2
# #     print(sum)

# # odd = 0
# # even = 0

# # for i in numbers:
# #     if i % 2==0:
# #         even+=i
# #     else:
# #         odd+=i

# # print(odd)
# # print(even)
# # 3) შექმენით პროგრამა სადაც პირველრიგში მომხმარებელი შემოიტანს რიცვხების რაოდენობას, შემდეგ for ციკლის გამოყენებით მაგდენი რიცხვი შემოატანინეთ input და ჩასვით სიაში

# # შემდეგ დაალაგეთ სიაში იპოვეთ მაქსიმალური და მინიმუალური რიცხვები (for ციკლის გამოყენებით აუცილებლად)

# li = []

# number = int(input("Enter how many: "))

# for k in range(number):
#     num = int(input(f"Enter number {k+1}: "))
#     li.append(num)

# print(li)

# if len(li)>0:
#     max=li[0]
#     min=li[0]
#     for num in li:
#         if num>max:
#             max=num
#         if num<min:
#             min=num
#     print(max)
#     print(min)
# else:
#     print("carieli sia")



# 4) მომხმარებელს შემოატანინეთ მოსწავლეების რაოდენობა (ერთი მთელი რიცხვი), შემდგომ მიეცით თითოეული მოსწავლისთვის ქულის შემოტანის შესაძლებლობა (ქულა 0-იდან 100-მდე) და თითოეული ქულა დაამატეთ მასივში, თქვენი დავალებაა, რომ გამოითვალოთ მთლიანი ჯგუფის (ყველა მოსწავლის) საშუალო ქულა, იპოვოთ მაქსიმალური ქულა და ასევე მინიმალური ქულა და საბოლოოდ უნდა დაითვალოთ რამდენმა მოსწავლემ ჩააბარა გამოცდა (ქულა 60-ზე მეტია) და რამდენმა ვერ ჩააბარა (ქულა 60-ზე ნაკლებია).

grade = []
students = int(input("How many student: "))
sul=0
max=0
min=0
gadasuli=0
chawrili=0
for i in range(1,students+1):
    score = int(input(f"Enter your score {i+1}: (0/100) "))

    while grade<0 or grade>100:
        print("Wrong!")
        score = int(input(f"Enter your score {i+1}: (0/100) "))
    grade.append(score)

for score in grade:
    sul+=score

    if grade>max:
        max=grade
    if grade<min:
        min=grade
    if grade > 60:
        gadasuli+=1
    if grade<60:
        chawrili+=1


print(max)
print(min)
print(gadasuli)
print(chawrili)
print(grade)