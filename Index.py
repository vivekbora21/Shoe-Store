from Cart import Cart
choice = 0
print("-----Welcome to The Shoe Store-----")
while(choice!=10):
    print('''0. Show All Items | 1. Buy Adidas | 2. Buy Nike | 3. Buy Reebok | 4. Buy Campus | 5. Buy Asics | 10.Checkout | 11. Show My Cart | 20.Admin portal''')
    try:
        choice = int(input("Pick your option: "))
        if(choice == 0):
            Cart.DisplayAll (self=0)

        elif(choice == 1):
            quantity = int(input("How many do you wish to buy? "))
            with open("item.txt",'r') as file:
                for i in file:
                    item = i.split()
                    if(item[0] == "Adidas"):
                        myCart = Cart(item[0],item[1],quantity)
                        cart = myCart.AddToCart(item,quantity)
                        if(cart == -1):
                            break
                        else:
                            bill = myCart.Bill(int(item[1])*quantity)
                            myCart.StockUpdate(i)
                            break
        
        elif(choice == 2):
            quantity = int(input("How many do you wish to buy? "))
            with open("item.txt",'r') as file:
                for i in file:
                    item = i.split(' ')
                    if(item[0] == "Nike"):
                        myCart = Cart(item[0],item[1],quantity)
                        cart = myCart.AddToCart(item,quantity)
                        if(cart== -1):
                            break
                        else:
                            bill = myCart.Bill(int(item[1])*quantity)
                            myCart.StockUpdate(i)
                            break
    
        elif(choice == 3):
            quantity = int(input("How many do you wish to buy? "))
            with open("item.txt",'r') as file:
                for i in file:
                    item = i.split(' ')
                    if(item[0] == "Reebok"):
                        myCart = Cart(item[0],item[1],quantity)
                        cart = myCart.AddToCart(item,quantity)
                        if(cart == -1):
                            break
                        else:
                            bill = myCart.Bill(int(item[1])*quantity)
                            myCart.StockUpdate(i)
                            break
        elif(choice == 4):
            quantity = int(input("How many do you wish to buy? "))
            with open("item.txt",'r') as file:
                for i in file:
                    item = i.split(' ')
                    if(item[0] == "Campus"):
                        myCart = Cart(item[0],item[1],quantity)
                        cart = myCart.AddToCart(item,quantity)
                        if(cart == -1):
                            break
                        else:
                            bill = myCart.Bill(int(item[1])*quantity)
                            myCart.StockUpdate(i)
                            break
        elif(choice == 5):
            quantity = int(input("How many do you wish to buy? "))
            with open("item.txt",'r') as file:
                for i in file:
                    item = i.split(' ')           
                    if(item[0] == "Asics"):
                        myCart = Cart(item[0],item[1],quantity)
                        cart = myCart.AddToCart(item,quantity)
                        if(cart == -1):
                            break
                        else:
                            bill = myCart.Bill(int(item[1])*quantity)
                            myCart.StockUpdate(i)
                            break
        elif(choice == 10):
            try:
                print("Do you wish to Checkout: ")
                response = input("Enter your Response: (y/n)")
                if(response.lower()=="y"):
                    myCart.Checkout(bill)
                    print("Your Bill is {} ".format(bill))
                    print('''------Thank You------''')
                elif(response.lower()=="n"):
                    choice = 0
                else:
                    print("Invalid Response")   
                    choice = 0
            except:
                print("You have not bought anything yet..")
                choice = 0
    
        elif(choice == 11):
            print("Items Added to Your Cart. ")
            Cart.ShowCart(self=0)
    
        elif(choice == 20):
            login = input("Enter Login Password")
            if(login == "1234"):
                print("-----Admin Page-----")
                print("Do you Wish To Update Stock?")
                response = input("Enter your Response----y/n: ")
                if(response == 'y'):
                    Shoe_name = input("Enter Which Shoe you want to add in stock: ")  
                    quantity = int(input("How many shoes you want to add: "))
                    found = False
                    with open("item.txt",'r') as fp:
                        for item in fp:
                            if(Shoe_name.lower() in item.lower()):
                                Cart.UpdateStock(0,Shoe_name,quantity)
                                found = True
                                break
                    if(found == False):
                        print("Record does not exist. Please try again.")
                            
                elif(response == 'n'):
                    choice = 0
                    print("Thank you.")
                else:
                    print("Invalid Choice. Please try Again.")
                                   
            else:
                print("Wrong Password")
        else:
            print("Invalid Choice. Please try Again.")
    except:
        print("Invalid Choice. Please try again.")
        
    
                       
       