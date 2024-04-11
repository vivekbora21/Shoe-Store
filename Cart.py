class Cart:
    
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.quantity = stock
        #self.items = [self.name,self.price,self.quantity]

    def DisplayAll(self):
        with open("item.txt",'r') as fp:
            tb = []
            print("-----------------------------")
            print("|Style  |Price  |In Stock|")
            print("-----------------------------")
            for line in fp:
                tb.append(line)
                disp = line.split()
                for p in disp:
                    print(p.ljust(7,' ')+"|", end =" ")
                print('\n')
    def ShowCart(self):
        with open("cart.txt","r") as fp:
            tb = []
            print("----------------------------")
            print("|Style  |Price  |Quantity|")
            print("----------------------------")
            for line in fp:
                tb.append(line)
                disp = line.split()
                for p in disp:
                    print(p.ljust(7,' ')+"|", end =" ")
                print('\n')

    def AddToCart(self,item,quantity):
        cart = ""
        if(int(item[2]) >= quantity and quantity > 0):
            item[2] = str(quantity) +'\n'
            for line in item:
               cart = cart+line+' '
            cart = cart.strip(' ')
            with open("cart.txt",'a') as fp:
                fp.write(cart)
        else:
            print("Oops! Available stock is {}. Please enter a valid number".format(item[2]))
            return -1
        
    def Bill(self,bill):
        with open("bill.txt",'r') as fp:
            for line in fp:
                line = line.strip()
        bill+=int(line)
        with open("bill.txt",'w') as fp:
            fp.write(str(bill))
            return bill
                
    def StockUpdate(self,buy):
        allItem = []
        ch = ""
        with open("item.txt","r") as fp:
            for item in fp:
                if(item!=buy):
                    allItem.append(item)
                else:
                    item = item.split()
                    item[2] = int(item[2])-self.quantity
                    item[2] = str(item[2])
                    for i in item:
                        ch = ch+i+' '
                    ch = ch.strip() + '\n'
                    allItem.append(ch)
                                    
        with open("item.txt","w") as fp:
            for line in allItem:
                fp.write(line)

    def Checkout(self,bill):
        with open("bill.txt",'w') as fp:
                fp.write('0')
        with open("cart.txt",'w') as fp:
            fp.write('')

    def UpdateStock(self,name,quantity):
        allItem = []
        with open("item.txt",'r') as fp:
            for line in fp:
                line = line.split(' ')
                if(name.lower() == line[0].lower()):
                    line[2] =int(line[2]) + quantity 
                    line[2] = str(line[2]) + '\n'
                    allItem.append(line)
                else:
                    allItem.append(line)

        with open("item.txt",'w') as fp:
            for item in allItem:
                line = ' '.join(item)
                fp.write(line)
        return
                
               



                    


    

    
        
