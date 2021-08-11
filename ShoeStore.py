def ShoeStoreThingy(PairOfShoes, PairOfSocks, Money, time):
#shoes#
    shoeBuy1 = int(input("How many Pairs of Shoe Would you like to buy, 1 pair of shoes = $800 ??? >>"))
    countshoe = PairOfShoes + shoeBuy1
    sureshoes = int(input("How Many shoes would you like to remove???, 0 for none >>"))
    countshoe = countshoe - sureshoes
    if countshoe < 0:
        countshoe = 0
    PairOfShoes = countshoe
    print("shoes =",PairOfShoes)
#End()#
    
#socks#
    shoeBuy2 = int(input("How many socks Would you like to buy, 1 pair of socks = $200 ??? >>"))
    countsocks = PairOfSocks + shoeBuy2
    suresocks = int(input("How Many socks would you like to remove???, 0 for none >>"))
    countsocks = countshoe - suresocks
    if countsocks < 0:
        countsocks = 0
    PairOfSocks = countsocks
    print("socks =",PairOfSocks)
#End()#
    checkPairOfSocks =int(input("Are you sure want to buy |1.Yes, 2.No| >>"))
    print(Money,"Money Budget left")
    if checkPairOfSocks == 1:
        checkshoes0 = 800 * PairOfShoes
        checkshoes1 = 200 * PairOfSocks
        shoesockprice = checkshoes0 + checkshoes1
        print(Money ,"= Money")
        time.sleep(2)
        if Money < shoesockprice:
            print("You don't have enough money, Cancelling the checkout")
        elif Money > shoesockprice:
            Money = Money - shoesockprice
            print("You have", Money ,"Budget Left")
    
