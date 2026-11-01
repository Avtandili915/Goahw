# 1) მომხმარებელს შემოაყვანინეთ თავისი სახელი, გვარი, ასაკი და საყვარელი ფერი, შემდგომ შექმენით ლისტი სახელად "user_info" და შეინახეთ ამ ლისტში მომხმარებლისმიერ შემოყვანილი ინფორმაცია.

# 2) შექმენით მასივი რომელშიც შეინახავთ მინიმუმ 10 სახელს, შემდგომ 3 მათგანი ჩაანაცვლეთ სხვა სახელებით პროგრამულად.

# 3) მოიძიეთ ინფორმაცია იმის შესახებ, თუ როგორ უნდა გადაუაროთ ლისტს for ციკლის დახმარებით, შემდგომ წინა დავალებაში შექმნილ ლისტს გადაუარეთ for ციკლის დახამრებით და გამოიტანეთ ყველა სახელი რიგ-რიგობით ტერმინალში.







name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

user_info = [name, surname, age, favorite_color]

print("User Info List:", user_info)









names_list = ["Nika", "Jina", "Luka", "Mariam", "Saba", "Salome", "Giorgi", "Elene", "Dato", "Nini"]

names_list[0] = "Avto"
names_list[3] = "Tamar"
names_list[7] = "Qeti"

print("Updated List:", names_list)



for name in names_list:
    print(name)