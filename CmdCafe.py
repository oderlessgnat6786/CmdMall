def FoodStoreLol(Money, time, im):
    print("What would you like to eat?")
    time.sleep(2)
    print("!Heres the menu!")
    time.sleep(2)
    im.show()
    time.sleep(2)
    eeee = input("Say Any Key to continue.")
    FoodList = []
    cash = 0
    time.sleep(5)
    for Loopies in range(3):
        order =int(input("What would you like|1.Fries $50, 2.Chicken $250, 3.Burger $500, 4.Drinks $10, 5.None $0| Pick any three!"))
        if order == 1:
            FoodList.append("Fries")
            print("Added Fries to the list")
            cash = cash + 50
        elif order == 2:
            FoodList.append("Chicken")
            print("Added Chicken to the list")
            cash = cash + 250
        elif order == 3:
            FoodList.append("Burger")
            print("Added Burger to the list")
            cash = cash + 500
        elif order == 4:
            FoodList.append("Drink")
            print("Added a Drink to the list")
            cash = cash + 10
        else:
            print("Added None To the list")
        print(cash ,"Is your food bill")
    print(FoodList ,"Here is your order")
    time.sleep(2)
    checkfood =int(input("Are you sure want to buy the food? |1.Yes 2.No| >>"))
    if checkfood == 1:
                   
        print("Ok... Purchasinng...")
        if Money < cash:
            print("Sorry, You dont have enough Money")
        elif Money > cash:
            Money = Money - cash
            print("Success!")
            time.sleep(2)
            print("Cooking Food...")
            time.sleep(10)
            print("Done!!!")
            time.sleep(1)
            print("Here is your food")
            print(FoodList)
            print("_____________________________")
            time.sleep(10)
    else:
        print("Ok cancelling the checkout")
