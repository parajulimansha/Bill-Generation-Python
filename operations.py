import read
import write

def valid_product_id():#validates the product ID entered by user and ensures it is valid
    """ ---The valid_product_id reads the laptop details from a file and prompts the user to enter a valid product ID.
for the laptop they want to buy.
        ---If an invad ID is entered, it prompts the user to enter a valid ID
is entered.
        ---Returns the valid ID entered by the user.
 """
    #reads laptop details from file
    laptop_inventory = read.read_laptop_details()
    read.display_laptop_details()
    loop = True
    while True:
        try:
            #takes product ID from user
            valid_id = int(input("Enter the product id of the product you would like to buy : "))

            #checks if product ID is valid
            while valid_id <= 0 or valid_id > len(laptop_inventory):
                print("Invalid ID!! Please enter a valid ID ")
                valid_id = int(input("Enter the valid product id of the product you would like to buy : "))

            #returns if product ID is valid
            return valid_id
        except Error:

            #prompts user to enter valid ID if any error occurs while getting product ID
            print("!!-- Only valid ID is accepted --!!")
            continue
#validates the quantity of laptops entered by the user and ensures that the quantity is available in stock
def valid_quantity(valid_id):
        #reads the laptop details from file
    """ ---The valid_quantity reads the laptop details from a file and prompts the user to enter the quanttiy
of laptops they want to buy for a given product ID.
        ---If an invalid quantity is entered, it prompts the user to enter a valid quantity until a valid quantity is entered.
        ---Returns the valid quantity entered by the user.
     """
    read.read_laptop_details()
    laptop_inventory = read.read_laptop_details()

    #gets quantity of laptops in stock
    quantity_in_stock = int(laptop_inventory[valid_id][3])
    loop = True
    while True:

        try:
            #takes quantity of laptops desired by the user
            user_quantity = int(input("Provide the quantity of laptop you want to buy : "))

            #checks whether desired quantity is available in stock
            while user_quantity <=0 or user_quantity > quantity_in_stock :
                print("Not enough quantity")

                user_quantity = int (input("Provide the quantity of laptop you want to buy : "))
            #returns if desired quantity is available in stock
            return user_quantity
        except Error:
            #prompts the user to enter a valid quantity if error in geting quantity
            print("The quantity you want to buy is not available. Provide quantity available in stock.")
            continue

#displays available products for selling and the user to buy a product
def products_for_selling():

    """---products_for_selling reads the laptop details from a file and prompts the user to select the product
they want to buy and its quantity.
        --- Updates the laptop inventory and generates a customer bill.
        ---Asks the user if they want to add more items andgenerates a final customer bill accordingly.
    """

    #set the status to purchase and prompts the user to purchase a laptop
    type_of_transaction = "Purchase"
    purchase_laptop = "yes"
    purchase_item = []
    print("\n")
    print("-" * 120 , "\n \n" )
    #displays available products for selling
    print("-" * 48 , "AVAILABLE PRODUCT LIST" , "-"*48 , "\n \n")
    print("-" * 120)

    while purchase_laptop == "yes":
        #reads the laptop details from the file and displays
        laptop_inventory = read.read_laptop_details()
          
        #takes the product ID and quantity of laptops desired by the user 
        laptop_id = valid_product_id()
        user_quantity = valid_quantity(laptop_id)
        
        #reduces quantity of laptops in stock by the number o laptops purchased 
        laptop_inventory[laptop_id][3] = int(laptop_inventory[laptop_id][3])-int(user_quantity)

        #updates laptop inventoryin the file
        write.update_laptop_inventory(laptop_inventory)

        #generates the customer bill for the purchased laptop
        y= write.purchase_item(laptop_inventory, laptop_id,user_quantity)

        #appends the customer bill to the list of purchased items        
        purchase_item.append(y)
        print(purchase_item)
       

        #prompt for the user to buy more laptops
        purchase_laptop = input("Want to add some more items ? (Yes/No) : ")
        
            

        #if the user doesnot want to purchase more laptop, then prompt to ship product is asked
        if purchase_laptop == "no":
             ship = input("Ship your product?(Yes/No) : ")

            #if no,bill is generated  without  shipping charge
             if ship == "yes":
                ship_price = 1000
                write.generate_customer_bill(purchase_item,ship_price, type_of_transaction)                
        #if yes, bill is generated with shipping charge
             else:
                ship_price = 0    
                write.generate_customer_bill(purchase_item,ship_price, type_of_transaction)                
         # if want to buy more items, purchase_laptop is set to yes        
        elif purchase_laptop == "yes":
            purchase_laptop = "yes"
        else:
            purchase_laptop = input("Please answer only in Yes/No")

def products_for_purchase():

    """---products_for_purchase displays the available product list and promptstheuser to select the product they want to
buy and its quantity.
        --- Updates the laptop inventory and generates a customer bill.
        ---Asks the user if they want to add more items andgenerates a final customer bill accordingly.
    """
    
    type_of_transaction = "buy"
    buy_laptop = "yes"
    buy_item = []
    #displays the available product list
    print("-" * 120, "\n \n")
    print("-" * 48 , "AVAILABLE PRODUCT LIST", "-" *48, "\n \n")
    print("-" * 120)

    #loop untl user doesn't want to purchase any more laptop
    while buy_laptop == "yes":

        #read laptop detail from file
        laptop_inventory = read.read_laptop_details()
        
        #asks user to select laptopid and quantity of laptop they want to buy
        laptop_id = valid_product_id()
        user_quantity = int(input("Enter quantity of laptops you want to buy: "))

        #update the laptop inventory after user's purchase
        laptop_inventory[laptop_id][3] = int(laptop_inventory[laptop_id][3])+int(user_quantity)

        #writes updated laptop inventory to the file
        write.update_laptop_inventory(laptop_inventory)

        #generates customer bill
        y= write.purchase_item(laptop_inventory, laptop_id,user_quantity)

        #appens the customer bill to buy_item list        
        buy_item.append(y)

        #asks user to buy more item or not 
        buy_laptop = input("Want to add some more items ? (Yes/No) : ")

        #if no then asks if user wants to ship the product
        if buy_laptop == "no":
            buy_laptop = "no"
            ship_price = 0
            write.generate_customer_bill(buy_item,ship_price,type_of_transaction)

        # if want to buy more items, buy_laptop is set to yes           
        elif buy_laptop == "yes":
            buy_laptop = "yes"
        else:
            buy_laptop = input("Please answer only in Yes/No")

