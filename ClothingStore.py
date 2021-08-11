def ShirtBuyClothing(Shirts, Pants, Money, time):
#Shirts#
    clothBuy1 = int(input("How many shirts Would you like to buy, 1 shirt = $500 ??? >>"))
    countshirt = Shirts + clothBuy1
    sureShirts = int(input("How Many shirts would you like to remove???, 0 for none >>"))
    countshirt = countshirt - sureShirts
    if countshirt < 0:
        countshirt = 0
    Shirts = countshirt
    print("Shirts =",Shirts)
#End()#
    
#Pants#
    clothBuy2 = int(input("How many pants Would you like to buy, 1 pant = $500 ??? >>"))
    countpants = Pants + clothBuy2
    surepants = int(input("How Many pants would you like to remove???, 0 for none >>"))
    countpants = countshirt - surepants
    if countpants < 0:
        countpants = 0
    Pants = countpants
    print("Pants =",Pants)
#End()#
    
#ClothingCheckout#
    checkclothes =int(input("Are you sure want to buy |1.Yes, 2.No| >>"))
    print(Money,"Money Budget left")
    if checkclothes == 1:
        checkclothes0 = 500 * Shirts
        checkclothes1 = 500 * Pants
        clothingprice = checkclothes0 + checkclothes1
        print(clothingprice,"Money")
        time.sleep(2)
        if Money < clothingprice:
            print("You don't have enough money, Cancelling the checkout")
        elif Money > clothingprice:
            Money = Money - clothingprice
            print("You have", Money ,"Budget Left")
        
    else:
        print("Ok Cancelling the checkout")
