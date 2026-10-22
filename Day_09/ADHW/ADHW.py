# დაბეჭდე რიცხვები 1-დან 10-ის ჩათვლით while ციკლის გამოყენებით.

start = 0 

while start < 10:
    start +=1
    print(start)


# დაბეჭდე რიცხვები 10-დან 1-ის ჩათვლით უკუთვლის პრინციპით.

start_num = 11

while start_num > 1:
    start_num -=1
    print(start_num)

# მომხმარებელს შემოატანინე სახელი და ეს სახელი 5-ჯერ დაბეჭდე while ციკლით.

user_name = input("Enter your name: ")

i = 0

while i < 5:
    print(user_name)
    i += 1


# გამოთვალე 1-დან 5-ის ჩათვლით ყველა რიცხვის ჯამი.

num1 = 1
sum = 0

while num1 <= 5:
    num1+=sum
    sum+=1
    print(num1)

# დაბეჭდე რიცხვი 2-ის გამრავლების ტაბულიდან პირველი 10 შედეგი.

start_gamravleba = 1
while start_gamravleba <= 10:
    shedegi = start_gamravleba *2
    print(shedegi)
    start_gamravleba +=1


# მომხმარებელს შემოატანინე რიცხვი და 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვი დაბეჭდე.

shemoiyvane = int(input("Enter Number: "))
j=1
while j <= shemoiyvane:
    print(j)
    j+=1

# while ციკლით დაბეჭდე ყველა ლუწი რიცხვი 2-დან 20-ის ჩათვლით.

dawyeba = 0

k = 0
while k <= 18:
    dawyeba+=k
    k+=2
    print(k)



# შექმენი saved_password ცვლადი, რომელშიც შეინახავ "python123" პაროლს. მომხმარებელს პაროლი იქამდე შემოატანინე, სანამ სწორად არ შეიყვანს.

saved_password = "avtojinajinaavto"

password_input = input("Enter your password: ")

while password_input != saved_password:
    print("Wrong, Try Again.")
    password_input = input("Enter your password: ")

print("Your in")



# დაბეჭდე რიცხვების კვადრატები 1-დან 5-ის ჩათვლით.

axlandeli = 5

while axlandeli <= 10:
    kvadrati = axlandeli ** 2
    print(kvadrati)
    axlandeli+=1


# მომხმარებელს შემოატანინე დადებითი რიცხვი და დაბეჭდე ყველა რიცხვი ამ რიცხვიდან 0-ის ჩათვლით.

dadebiti = int(input("Enter possitive number: "))


while dadebiti >= 1:
    dadebiti-=1
    print(dadebiti)