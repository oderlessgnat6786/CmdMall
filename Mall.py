from ClothingStore import *
from ShoeStore import *
from CmdCafe import *
from GroceriesStore import *
import time
from PIL import Image, ImageFilter

im = Image.open("CmdCafeMenu.png")
#Datastore Services / Gear#
Money = 10000
PairOfShoes = 0
PairOfSocks = 0
ShoeThingsLolXd = PairOfShoes + PairOfSocks
Shirts = 0
Pants = 0
Clothes = Shirts + Pants
Groceries = 0
Bags = [ShoeThingsLolXd,Clothes,Groceries]
hours = 5
shirtprice = 500
pantprice = 500
groceryprice = 100
#BootUp#
print("*******************************!!Welcome!!************************************")
time.sleep(1)
print("Entering")
time.sleep(2)
print("You have", Money,"as budget, use it wisely.")
time.sleep(2)
hoursShopping=int(input("How many Hours Do you want to Shop >>"))
time.sleep(2)
        
#The main purpose of this file LOLLLLLLLLLLL! xd stupid text lol continue noob jk!!#
for x in range(hours):
    hours = hoursShopping
    print("You can shop for", hours,"hours")
    print("Where Would You like to go???")
    room =int(input("|1.ClothingCentre, 2. ShoeStore, 3.CMDCafe, 4.Groceries| >>"))
    
#Stores Moment Lol#
#Clothing Centre#
    if room == 1:
        ShirtBuyClothing(Shirts, Pants, Money, time)
#Shoe Store#
    elif room == 2:
        ShoeStoreThingy(PairOfShoes, PairOfSocks, Money, time)
    elif room == 3:
        FoodStoreLol(Money, time, im)
    elif room == 4:
        FoodPlsImHomeLess(Money, time, Groceries, groceryprice)
    else:
        print("We dont have that here")
    hoursShopping = hours - 1
    if hours < 0:
        break
print("Your Shopping Bill list is", Bags ,", the Total you have is", Money ,"remaining.")
time.sleep(5)
print("Your Shopping Session Has Ended, You can visit again if you want to.")
