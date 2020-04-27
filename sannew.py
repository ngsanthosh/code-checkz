mobiles=["Redmi note 7 pro","samsung M30s","Realme XT"]
def gen():
    b=int(input("Select Which of the categorie you need to buy \n 1.Mobile phone \n 2.Tablets \n 3.Accessories"))
    if(b==1):
        print("We're currently stocking only 3 mobile phones, Select any of the phone and all are of Rs.15000")
        print(mobiles)
        print("Still The data is being analyzed.. So wait for a week")
    else:
        print("We are still in the developement stage... Try again later..")
def maa():
    print("Welcome to Santhosh's E-shopping")
    gen()
def ixm():
    print("Thank you... Enjoy Shopping with us..")
    gen()
def tri():
    print("Thank you... Enjoy shopping with us..")
    gen()
def cbe():
    print("Thank you... Enjoy shopping with us..")
    gen()
    

def doso():
    a=int(input("Select which city youre from \n1.Chennai \n2.Madurai \n3.Trichy \n4.coimbatore \n And Press any other key if none of the above"))
    if(a==1):
       maa()
    elif(a==2):
       ixm()
    elif(a==3):
       tri()
    elif(a==4):
       cbe()
    else:
       print("Sorry!, Currently our service is unavailable in your city...We'll Meet soon")

print("Welcome to Santhosh online shopping store \nCaution: YOUR IP ADDRESS IS BEING MONITORED FOR SECURITY PURPOSE!")  #program written by Santhosh
print("Provide the username and password as on the membership-card to get in.")
un=input("Username:")
psw=input("Password:")
if(un=="000" and psw=="000"):
    print("You are Successfully Signed in :)")
    doso()
else:
    print("Incorrect username or password")


    
