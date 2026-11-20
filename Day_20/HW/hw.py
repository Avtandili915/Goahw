# 2) შექმენით პროგრამა, რომელშიც თავდაპირველად იქნება 6 სხვადასხვა ხილი Set-ის სახით. 
# მომხმარებელს შეაყვანინეთ ახალი ხილის სახელი და გამოიყენეთ add() მეთოდი მის დასამატებლად. საბოლოოდ დაბეჭდეთ განახლებული Set.

fruit = {"Orange", "Banana", "Apple", "Bali", "Vafslatama", "Marwyvi"}
print(fruit)
fruit.add("Dragon fruit")
print(fruit)


# 3) შექმენით მოსწავლეების Set, რომელშიც მინიმუმ 5 მოსწავლის სახელი იქნება.
# მომხმარებელს შეაყვანინეთ მოსწავლის სახელი და in ოპერატორის გამოყენებით შეამოწმეთ, არის თუ არა ეს მოსწავლე Set-ში.
# შესაბამისი შედეგი დაბეჭდეთ ტერმინალში.

students = {"Avto", "Jina","Nene","Sesili","Data"}
user_student = input("Enter your name: ")

if user_student in students:
    print("Shen xar!")
else:
    print("Shen ar xar")

# 4) შექმენით რიცხვების Set, რომელშიც მინიმუმ 7 სხვადასხვა რიცხვი იქნება.
# მომხმარებელს შეაყვანინეთ რიცხვი და შეამოწმეთ, არის თუ არა ის Set-ში. შემდეგ გამოიყენეთ remove() მეთოდი ამ რიცხვის Set-იდან წასაშლელად.
# საბოლოოდ დაბეჭდეთ განახლებული Set.

num = {9,915,15,10,13,18,21}
user_num = int(input("Enter ur number: "))
if user_num in num:
    print("Aris!")
    num.remove(user_num)
else:
    print("Araris!")
print(num)

# 5) შექმენით ცხოველების Set, რომელშიც მინიმუმ 6 სხვადასხვა ცხოველი იქნება. გამოიყენეთ len() ფუნქცია, რათა გაიგოთ, რამდენი ელემენტია Set-ში.
# შემდეგ მომხმარებელს შეაყვანინეთ ახალი ცხოველის სახელი და add() მეთოდის გამოყენებით დაამატეთ Set-ში.
# საბოლოოდ დაბეჭდეთ განახლებული Set და მისი სიგრძე.

animal = {"Cow", "Dog", "Cat", "Giraffe", "Tiger", "Crocodille"}
print(len(animal))
axali_animal = input("Enter new animal!")
animal.add(axali_animal)
print(animal)


# 6) შექმენით პროგრამა, რომელშიც თავდაპირველად იქნება 5 სხვადასხვა ფერის Set.
# მომხმარებელს შეაყვანინეთ ორი ფერის სახელი. გამოიყენეთ in ოპერატორი, რათა შეამოწმოთ, არის თუ არა ორივე ფერი Set-ში.
# თითოეული შემოწმების შედეგი ცალ-ცალკე დაბეჭდეთ ტერმინალში.


color = {"Red", "Orange", "Purple", "Yellow", "Black"}
colorr = input("Enter First Color: ")
colorrr = input("Enter Second Color: ")
if colorr and colorrr in color:
    print("Orive feri aris!")
else:
    print("Arcerti")