# 2) შექმენით ხილის Tuple, რომელშიც მინიმუმ 6 სხვადასხვა ხილი იქნება. დაბეჭდეთ Tuple-ის პირველი, მესამე და ბოლო ელემენტები. 
# საბოლოოდ გამოიტანეთ Tuple-ის სრული სიგრძე len() ფუნქციის გამოყენებით.


# fruit = ("Apple", "Orange," "Mandarine", "Painiple", "Banana", "Kiwi")
# print(fruit[0])
# print(fruit[2])
# print(fruit[-1])
# print(len(fruit))


# 3) შექმენით მოსწავლეების Tuple, რომელშიც მინიმუმ 5 მოსწავლის სახელი იქნება. 
# მომხმარებელს შეაყვანინეთ მოსწავლის სახელი და შეამოწმეთ in ოპერატორის გამოყენებით, არის თუ არა ეს მოსწავლე Tuple-ში. 
# შესაბამისი შედეგი დაბეჭდეთ ტერმინალში.

# students = ("Avto", "Jina", "Nini", "Nene", "Gabriel")
# user = input("Enter your name: ")
# for i in students:
#     if i.lower()==user.lower():
#         print("Ur correct student!")
#         break

# 4) შექმენით რიცხვების Tuple, რომელშიც მინიმუმ 7 რიცხვი იქნება. გამოიყენეთ count() მეთოდი, რათა გაიგოთ, რამდენჯერ მეორდება კონკრეტული რიცხვი Tuple-ში
# ასევე გამოიყენეთ index() მეთოდი, რათა იპოვოთ ამ რიცხვის პირველი გამოჩენის ინდექსი.

# num = (9,915,159,195,915,9,0)
# n = num.count(9)
# m = num.index(915)
# print(n)
# print(m)


# 5) შექმენით ქალაქების Tuple, რომელშიც მინიმუმ 6 ქალაქი იქნება. გამოიყენეთ slicing, რათა დაბეჭდოთ Tuple-ის 
# პირველი სამი ელემენტი, შემდეგ კი ბოლო სამი ელემენტი. საბოლოოდ დაბეჭდეთ მთლიანი Tuple.

# city = ("Paris", "Barcelona", "Abasha", "Gardabani", "Madrid", "Prague")
# print(city[0:3])
# print(city[-3:])