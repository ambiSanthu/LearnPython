class Inventory():
    def __init__(self,country,price):
        self.country = country
        self.price = price
    def ipodCost(self,numOfItems):
        return (self.price * numOfItems)
    def transitcharge(self,numOfItems):
        transitCharge = 400 * (numOfItems//10)   
        actualPrice = self.ipodCost(numOfItems)
        return (transitCharge + actualPrice)
    
    
def main():        
    while(True):
        user_input=input("Enter Country Name and number of ipos required. Enter STOP to exit...")
        if user_input == "STOP":
            break
            
        country = user_input.split(':')[0].strip()
        numOfItems = int(user_input.split(':')[1].strip())
        if numOfItems > 200:
            print("Out of stock!!!")
        elif numOfItems > 100:
            numOfItems = numOfItems - 100
            if numOfItems < 10:
                print("Order Not Possible !!!")
                continue
            totalCost_brazil = BrazilInventory.ipodCost(100) + ArgentinaInventory.transitcharge(numOfItems)
            totalCost_arg = ArgentinaInventory.ipodCost(100) + BrazilInventory.transitcharge(numOfItems)
            if totalCost_brazil < totalCost_arg:
                print("{0} : {1} : {2}".format(totalCost_brazil,0,100-numOfItems))
            else:
                print("{0} : {1} : {2}".format(totalCost_arg,100-numOfItems,0))
        else:
            if country == "Brazil":
                totalCost_brazil = BrazilInventory.ipodCost(numOfItems)
                if numOfItems > 10:
                    totalCost_arg = ArgentinaInventory.transitcharge(numOfItems)
                else:
                    print("{0} : {1} : {2}".format(totalCost_brazil,100-numOfItems,100))
                    continue
            else:
                if numOfItems > 10:
                    totalCost_brazil = BrazilInventory.transitcharge(numOfItems)
                else:
                    totalCost_arg = ArgentinaInventory.ipodCost(numOfItems)
                    print("{0} : {1} : {2}".format(totalCost_arg,100,100-numOfItems))
                    continue           
            if totalCost_brazil < totalCost_arg:
                print("{0} : {1} : {2}".format(totalCost_brazil,100-numOfItems,100))
            else:
                print("{0} : {1} : {2}".format(totalCost_arg,100,100-numOfItems))

            
    
if __name__ == "__main__":
    BrazilInventory = Inventory('Brazil',100)
    ArgentinaInventory = Inventory('Argentina',50)
    main()
        
