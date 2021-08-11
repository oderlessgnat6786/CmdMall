def FoodPlsImHomeLess(Money, time, Groceries, groceryprice):
#Shirts#
    bobobobo = int(input("How many Groceries Would you like to buy, 1 Grocery = $100 ??? >>"))
    countpls = Groceries + bobobobo
    sureGroceries = int(input("How Many Groceries would you like to remove???, 0 for none >>"))
    countpls = countpls - sureGroceries
    if countpls < 0:
        countpls = 0
    Groceries = countpls
    print("Groceries =",Groceries)
#End()#
    
#ClothingCheckout#
    checkclothes =int(input("Are you sure want to buy |1.Yes, 2.No| >>"))
    print(Money,"Money Budget left")
    if checkclothes == 1:
        checkclothes0 = 100 * Groceries
        clothingprice = checkclothes0
        print(clothingprice,"Money")
        time.sleep(2)
        if Money < clothingprice:
            print("You don't have enough money, Cancelling the checkout")
        elif Money > clothingprice:
            Money = Money - clothingprice
            print("You have", Money ,"Budget Left")
        
    else:
        print("Ok Cancelling the checkout")
