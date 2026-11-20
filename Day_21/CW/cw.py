# 7) შექმენით ფუნქციოა სახელად multiply რომელსაც გადაეცემა 
# ერთი პარამეტრი სახელად operation ეს multiply ფუნქცია აბრუნებს 2 * operation(5, 10)

# შემდეგ შექმენით რომელიმე მათემატიკური ფუნქცია add, 
# subtract, divide რომელსაც გადაეცემა 2 პარამეტრი num1, num2

# როდესაც შექმნით ფუნქციას გამოიძახეთ multiply და გადაეცით მეორე ფუნქცია მნიშვნელობად

# საბოლოოდ დაბეჭდეთ multiply ფუნქციიდან დაბრუნებული მნიშნელობა

def mul(opr):
    return 2 * opr(5,10)
def damateba(num1, num2):
    return num1+num2
shedegi=mul(damateba)
print(shedegi)


# შექმენით ფუნქცია სახელად calculateBonus, რომელსაც გადაეცემა ერთი პარამეტრი სახელად action. ეს ფუნქცია აბრუნებს action(100, 20) + 50-ს.

# შემდეგ შექმენით რომელიმე მათემატიკური ფუნქცია (add, subtract ან multiply), რომელსაც გადაეცემა 2 პარამეტრი: a და b.

# როდესაც შექმნით მეორე ფუნქციას, გამოიძახეთ calculateBonus და არგუმენტად (მნიშვნელობად) გადაეცით ეს მეორე ფუნქცია.

# საბოლოოდ, დაბეჭდეთ calculateBonus ფუნქციიდან დაბრუნებული შედეგი.

def calbo(action):
    return action(100,20) +50
def mult(a,b):
    return a*b
she=calbo(mult)
print(she)


# შექმენით ფუნქცია სახელად formatText, რომელსაც გადაეცემა ერთი პარამეტრი სახელად textModifier. ეს ფუნქცია აბრუნებს textModifier("გამარჯობა", "სამყარო") + "!"-ს.

# შემდეგ შექმენით ფუნქცია სახელად combineWords, რომელსაც გადაეცემა 2 პარამეტრი: word1 და word2 (ეს ფუნქცია უნდა აერთებდეს ამ ორ სიტყვას შუაში გამოტოვებით/სფეისით).

# როდესაც შექმნით მეორე ფუნქციას, გამოიძახეთ formatText და არგუმენტად გადაეცით combineWords ფუნქცია.

# საბოლოოდ, დაბეჭდეთ formatText ფუნქციიდან დაბრუნებული შედეგი.

def forr(text):
    return text("Hello", "World") + "!"
def comb(word1,word2):
    return word1+ " "+ word2
pasuxi=forr(comb)
print(pasuxi)