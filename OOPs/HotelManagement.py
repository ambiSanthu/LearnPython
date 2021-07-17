class Hotel():
    def __init__(self,name,rating,cust_type):
        self.name = name
        self.rating = rating
        self.customer_type = cust_type

class Pricing(Hotel):
    def setPrice(self, wd_rate, we_rate):
        self.weekday_rate = wd_rate
        self.weekend_rate = we_rate
    def getPrice(self,day):
        if day.lower() in ['sun','sat']:
            return self.weekend_rate
        else:
            return self.weekday_rate
    def printDetails(self):
        print("Hotel Name : ", self.name)
        print("Customer Type : ", self.customer_type)
        print("Weekday Price: ", self.weekday_rate)
        print("Weekend Price: ", self.weekend_rate)
    
def getCustPrice(name,custtype,day):
    if custtype == 'regular':
        if name == 'x':
            return X_Regular.getPrice(day)
        elif name == 'y':
            return Y_Regular.getPrice(day)
        elif name == 'z':
            return Z_Regular.getPrice(day)
    elif custtype == 'rewardee':
        if name == 'x':
            return X_Rewardee.getPrice(day)
        elif name == 'y':
            return Y_Rewardee.getPrice(day)
        elif name == 'z':
            return Z_Rewardee.getPrice(day)
    else:
        return None
      
def main():
    while (True):
        user_input = input("Enter Customer Type and Dates and Enter STOP to exit : ")
        if user_input == 'STOP':
            print("Exiting...")
            break
        custtype = user_input.split(":")[0]
        print("Customer Type : ",custtype)
        dates = user_input.split(":")[1]

        for cust in dates.split(","):  
            day = cust.split("(")[1].replace(')','')
            date = cust.split("(")[0]
            x_price = getCustPrice('x',custtype,day)
            y_price = getCustPrice('y',custtype,day)
            z_price = getCustPrice('z',custtype,day)
            
            if not x_price or not y_price or not z_price:
                print("Enter Valid Input")
                continue

            #print(x_price,y_price,z_price)
            minprice = min(x_price,y_price,z_price)
            if minprice == y_price:
                print("For {0}, Hotel y is the best option with the total cost of ${1}".format(date,minprice))
            elif minprice == z_price:
                print("For {0}, Hotel z is the best option with the total cost of ${1}".format(date,minprice))
            else:
                print("For {0}, Hotel x is the best option with the total cost of ${1}".format(date,minprice))
        
        
if __name__ == "__main__":
    X_Regular = Pricing('x',3,'regular')
    X_Regular.setPrice(100,120)
    #X_Regular.printDetails()
    X_Rewardee = Pricing('x',3,'rewardee')
    X_Rewardee.setPrice(90,60)
    #X_Rewardee.printDetails()

    Y_Regular = Pricing('y',5,'regular')
    Y_Regular.setPrice(130,150)
    #Y_Regular.printDetails()
    Y_Rewardee = Pricing('y',5,'rewardee')
    Y_Rewardee.setPrice(100,95)
    #Y_Rewardee.printDetails()

    Z_Regular = Pricing('z',4,'regular')
    Z_Regular.setPrice(195,150)
    #Z_Regular.printDetails()
    Z_Rewardee = Pricing('z',4,'rewardee')
    Z_Rewardee.setPrice(120,90)
    #Z_Rewardee.printDetails()
    main()
