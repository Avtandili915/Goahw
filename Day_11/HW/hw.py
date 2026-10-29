dadasturebuli = 0
uaryofa = 0
momxmarebeli = 0
starting_price = 2.50
km_price = 0.70
taxi_sum = 0
night_drive = "20%"
night_drive2 = 0.20
tree_for = 3

total_kms = 0
total_xalxi = 0


for i in range(1, momxmarebeli+1):
    sul_ramdeni_momxmarebeli= int(input(f"Enter how many {momxmarebeli} do u have: "))

while True:
    print("======= TAXI SYSTEM =======")
    print("1. მგზავრობის შეკვეთა")
    print("2. შემოსავლის ნახვა")
    print("3. მგზავრობების სტატისტიკა")
    print("4. გასვლა")
    print("===========================")

    choice = int(input("Enter number: "))

    if choice ==1:
        print("Diliverys Starting price is: ", starting_price)
        print("Km price is :", km_price)
        print("Night Drive damatebiti price is :", night_drive)
        xalxi = int(input("Enter how many people are in: "))
        km = int(input("Enter how mane km do u wana to rade: "))
        dgis_mona = input("Night drive (Yes/No)")
        
        if xalxi>4 and xalxi <=0:
            xalxi = int(input("Enter how many people are in: "))
        if km!=0:
            km = int(input("Enter how mane km do u wana to rade: "))
        if xalxi ==3 or xalxi ==4:
            taxi_sum+=tree_for
        if dgis_mona=="Yes" or dgis_mona=="yes":
            taxi_sum*=night_drive2
        elif dgis_mona=="No" or dgis_mona=="no":
            pass
        else:
            dgis_mona = input("Night drive (Yes/No):")

        unda_mgzavroba= input("Do you want to accept drive (Yes/No): ")
        if unda_mgzavroba =="Yes" or unda_mgzavroba=="yes":
            print("Mgzavroba mimdinareobs.")
            total_kms+=km
            total_xalxi+=1
            dadasturebuli+=1
            print(km, xalxi, dgis_mona)
        else:
            print("Mgzavroba Chaishala!")
            uaryofa+=1
            
    
    elif choice ==2:
        taxi_sum+=km_price*total_kms
        print(taxi_sum // 1)
    elif choice ==3:
        print("Cven gaviaret", total_kms)
        print("Cven gvyavda", total_xalxi)
        print("Cven vishovet", taxi_sum)
        print("Dadasturda", dadasturebuli)
        print("Uaryofil iqna", uaryofa)
        if dadasturebuli!=0:
            print(taxi_sum / dadasturebuli)
    elif choice ==4:
        print("Gmadlobt rom sargeblobt cvenit <3")
        break
    else:
        print("Incorect number, Try again!")
        choice = int(input("Enter number: "))
    




