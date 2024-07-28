#importing the datetime module to get the current date and time

import datetime #uniquename_for_txt = year + month+ day + second + hours + name


def update_laptop_inventory(laptop_inventory):
    """Updates the laptop inventory by writting the current inventory data to file.

    Parameters:
    laptop_inventory(dict) : a dictionary containing the laptop inventory data, where the keys are the product ids and the values are lists containing the product (name, description, price, quantity, brand and model)

    Returns:
    dict: the updated laptop inventory
"""

 
    file = open("laptop.txt", "w")#opens the fle "laptop.txt" in write mode. This overrites the existing file
    for laptop in laptop_inventory.values(): # loops through all the laptops in the inventory dictionary
        file.write(str(laptop[0])+ "," + str(laptop[1])+ "," + str(laptop[2])+ "," + str(laptop[3])+ "," + str(laptop[4])+ "," + str(laptop[5])) #writes each laptops data to a new line in the file
        file.write("\n") #adds new line after writing each laptops data to the file
     
    return (laptop_inventory) # return the updated laptop inventory dictionary



def purchase_item(laptop_inventory, valid_id, quantity):

    """Adds the purchased item to a list of customer items.

    Parameters:
    laptop_inventory(dict) : a dictionary containing the laptop inventory data, where the keys are the product ids and the values are lists containing the product (name, description, price, quantity, brand and model)
    valid_id(str) : the product id of the item being purchased.
    quantity(int): the quantity of the item being purchased.

    Returns:
    list : Contains the name, quantity, price, and total price of the purchased item.

    ---The function takes dictionary 'laptop_inventory' containing the laptop data, a string 'valid_id' representing the ID of the product being purchased, and an integer 'quantity' representng the quantity of the product being
        purchased. Returns list containing the name, quantity, price, and total price of purchased item.

    ---First, extracts the name quantirt and prce and purchased item from the dictionary using 'valid_id' parameter.
    
    ---Removes '$' sign from the price converts to integer, multiplies by the quantity, and assigns the result to 'total_price'.
    
"""


    #get the name, quantity, and price of the purchased item
    product_name = laptop_inventory[valid_id][0]
    product_quantity = quantity
    product_price = laptop_inventory[valid_id][2].replace("$","")
    total_price = int(quantity) * int(product_price)

    #storing users purchased item

    purchase_items_list=[]
    purchase_items_list.append(product_name)
    purchase_items_list.append(product_quantity)
    purchase_items_list.append(product_price)
    purchase_items_list.append(total_price)
    print(purchase_items_list)
    return purchase_items_list

def generate_customer_bill(purchase_items_list,ship_price,type_of_transaction):
    """Generates a customer bill for the purchased items.

    Parameters:
    purchased_items_lst(list): a list containing the name,quantity, price, and total price of each purchased item.
    cost_for_shipping(int): cost of shipping (if any).
    type_of_transaction(str): the type of transaction(either "purchase" or "return").

    Raises:
    ValueError:
    if name, number or address input by the user is empty.

    Description:
 ---The function takes a list o purchased items, the shipping cost (if any), and the type o transaction and generates an
    invoice for the custmer's purchase.
 ---The invoice includes details of the purchased items, the buyer's name, phone number,
    and address, the purchase date, the total amount due, and the shipping cost(if any). If the transaction is a return, the
    invoice shows only the details of the items being returned and the total amount due.
---The function also writes the invoice to a file named "customer_bill.txt".
 The purchased_items_list should be a ist of lists, where each inner list contains the details of a single purchased item.""" 
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month) 
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour) 
    minutes = str(datetime.datetime.now().minute)  
    second = str(datetime.datetime.now().second)

    date_bill_generation = year + month+ day + hours + minutes + second   

    #getting values for bill generation
    print("---------------------------------------------------------------------------------------------------------------------------------\n\n")
    print("Provide the required details below to make bill : ")
    name = input("Enter your name : ")
    
    #try except for phone number
    is_valid_phone_num = False

    #looping until a valid phone number is entered
    while not is_valid_phone_num:

    #asking user to input their phone number
        phone_num = input("Enter your phone number : ")

    #checking if the phone number is composed entirely of digits
        if phone_num.isdigit():
            is_valid_phone_num = True
        else:
    #error message thrown if phone number is not valid
            print("Provide valid phone number!")
            continue



    #bill
    uniquename_for_txt = date_bill_generation+"_"+name+"_"+str(phone_num)
    print("---------------------------------------------------------------------------------------------------------------------------------\n\n")
    print("---------------------------------------------  MANSHA ELECTRONICS  ------------------------------------------------------------------")
    print("------------------------------------------  GAUSHALA, KATHMANDU ----------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------------------------------\n\n")
    if type_of_transaction == "Purchase": #invoiceon screen or selling the laptops
        print("Name: " + name)
        print("Phone Number: " +str(phone_num))
        print("Date: " +year +"/"+ month+"/"+ day+"\n\n")
        
        print("S.N \t Name \t \t Quantity \t Price \t\t\t Total")
        serial_number = 1
        Grand_total = 0 + ship_price
        for values in purchase_items_list:
            print(serial_number ,"\t", values[0],"\t", values[1],"\t\t","$" , values[2],"\t\t", "$" ,values[3])
            serial_number = serial_number + 1
            Grand_total = Grand_total + values[3]
        print("\n")
        if ship_price == "yes":
            print("\t \t \t \t  Your Total :\t \t \t" , "$" , str(Grand_total))

        else:
            print("\t \t \t \t  Shipping Cost :\t \t \t" , "$" , str(ship_price))
            print("\t \t \t \t  Your Grand Total   :\t \t \t" , "$" , str(Grand_total))
            print("\n\n\n")
         
    else:
        #invoice on screen for buying the laptops
        print("Name " + name)
        print("Phone Number: " +str(phone_num))
        print("Date: " +year +"/"+ month+"/"+ day+"\n\n")
        print("S.N \t Name  \t\t Quantity \t Price \t\t\t Total")
        serial_number = 1
        total = 0 
        for values in purchase_items_list:
            print(serial_number ,"\t", values[0],"\t","\t\t", values[1],"\t\t","$" , values[2],"\t\t", "$" ,values[3])
            serial_number = serial_number + 1
            total = total + values[3]
        print("\n")
        vat_amount= total*(13 / 100)
        Grand_total = vat_amount + total
        
        print("\t \t \t \t  Total :\t \t \t \t" , "$" ,str(total))
        print("\t \t \t \t  Vat amount :\t \t \t \t" , "$" ,str(vat_amount))
        print("\t \t \t \t  Amount after VAT   :\t \t \t" , "$" ,str(Grand_total))
        print("\n\n\n")
    #text file for the bill
    file = open(str(uniquename_for_txt)+".txt","w")
    file.write("                                   MANSHA ELECTRONICS \n\n")
    file.write("                                   GAUSHALA, KATHMANDU  \n\n\n")
    file.write("                                       9863444458    \n\n")
    file.write("Name: " + name)
    file.write("\n")
    file.write("Phone Number: " +str(phone_num))
    file.write("\n")
    file.write("Date: " +year +"-"+ month+"-"+ day+"\n\n")
    file.write("S.N \t Name \t\t  Quantity   \t\tPrice \t\tTotal")
    file.write("\n")
    
    if type_of_transaction == "Purchase": #bill for selling laptops 
        serial_number = 1
        Grand_total = 0 + ship_price
        for values in purchase_items_list:
            file.write(str(serial_number) +"\t"+ str(values[0])+"\t" +"\t"+ str(values[1])+"\t\t"+ str(values[2])+"\t\t"+ str(values[3]))
            serial_number = serial_number + 1
            Grand_total = Grand_total + values[3]
            file.write("\n")
        file.write("\n")
        if ship_price == 0:
            file.write("\t \t \t \t  Your Grand Total :\t \t \t" +"$" + str(Grand_total))
            file.write("\n")

        else:
            file.write("\t \t \t \t  Your Shipping Cost :\t \t \t" + str(ship_price))
            file.write("\n")
            file.write("\t \t \t \t  Your Grand Total   :\t \t \t" + str(Grand_total))
            file.write("\n")
            file.write("\n\n\n")
    else:
        #Bill for buying laptops
        serial_number = 1
        total = 0 
        for values in purchase_items_list:
            file.write(str(serial_number) +"\t"+ str(values[0])+"\t"+"\t"+ str(values[1])+"\t\t"+ str(values[2])+"\t\t"+ str(values[3]))
            serial_number = serial_number + 1
            total = total + values[3]
            file.write("\n")
        file.write("\n")
        vat_amount= total*(13 / 100)
        Grand_total = vat_amount + total
        
        file.write("\t \t \t \t   Total :   \t \t \t \t" + str(total))
        file.write("\n")
        file.write("\t \t \t \t  Vat amount added :\t\t\t " + str(vat_amount))
        file.write("\n")
        file.write("\t \t \t \t  Amount after VAT   :\t \t \t" + str(Grand_total))
        file.write("\n")
        file.write("\n\n\n")
    file.close()




























    
   
"""

#converting the year, month, dat, hours, minutes, and seconds to strings for concentration
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour) 
    minutes = str(datetime.datetime.now().minute) 
    second = str(datetime.datetime.now().second)

#generating a unique code for the bill based on the current date and phone number entered by the user

    date_bill_generation = year + month + day + hours + minutes + second
    
# printing the header for bill
    print("-" *85)
    print("Provide the required details below to make bill : ")

   

#asking user to input their name and checking if the input is empty
    name = input ("Enter your Name : ")
   
    
#asking user to input their address and checking if the input is empty    
    address = input("Enter address of the customer : ")
    
    
#initializing a lag variable to check if the phone number entered by the user is valid
    is_valid_phone_num = False

#looping until a valid phone number is entered
    while not is_valid_phone_num:

#asking user to input their phone number
        phone_num = input("Enter your phone number : ")

#checking if the phone number is composed entirely of digits
        if phone_num.isdigit():
            is_valid_phone_num = True
        else:
#error message thrown if phone number is not valid
            print("Provide valid phone number!")
            continue

        #generating a unique bill code for the screen display based on the phone number and the date and time of bill generation

    _bill_generation_ = str(phone_num)+"/"+date_bill_generation

        #priniting invoice header

    print("-" * 85)
    print("-" * 35 + " Mansha Electronics" + "-" * 35)
    print("-" * 85)
    print("Buyer: " + str(name))
    print("Phone Number: " + str(phone_num))
    print("Address: " + str(address))
    print("Purchased Date: " + day + "/" + month + "/" + year )
    print("S.N \t Product Name \t\t Purchased Quantity \t\t Rate \t\tTotal Price")
        # checking if the transaction type is "purchase"
    if type_of_transaction == "purchase":
            


        #initializing the serial number and total variables
        serial_number = 1
        total = 0 + ship_price
        #looping through the lst of purchased items and printing their details
        for values in purchased_items_list:
            print(serial_number," " , values[0], " " , values[1], " " ,values[2], " " , values[3])

        #incrementing the serial number and total cost variables
            serial_number+= 1
            total += int(values[3])
            print(total)

        #printing the final total or the total amount with shipping cost
        if ship_price == 0:
            print("Final Total : " , str(total))
        else:
            print("Shipping Cost : ", ship_price )
            print("Total Amount: " , total )
    else:
            
        serial_number = 1
        total = 0
            
        #iterates through each purchaesd tem in the purchased_item_list.
        for values in purchased_items_list:
                
                #prints the details of the item.
            print(serial_number,"\t\t " , values[0], " \t\t" , values[1], " \t\t" ,values[2], " \t\t" , values[3])

                #increment the serial_number variable.
            serial_number += 1

                #adding the items price to the total variable.
            total += values[3]
                
            #calculates the amount after vat and the total cost after vat.

        amount_after_vat = total_cost * (13/100)
        totalcost_after_vat = amount_after_vat + total_cost

            #prints the total cost, amount after vatt, and total cost after vat
        print("Total: " ,str(total))
        print("Amount when vat added: " ,str(amount_after_vat))
        print("Total cost after VAT added :  ", str(totalcost_after_vat))


            #invoice for bill_file
            # horizontal line to seperate sectons of invoice.
            
        file = open(str(uniquename_for_txt)+".txt","w")
        file.write("-" * 85)
        file.write("-" * 35 + " Mansha Electronics" + "-" * 35) #name of store
        file.write("-" * 85)
            #buyer's name, phone number, address and purchase date
        file.write("Buyer: " + name)
        file.write("Phone Number: " + str(phone_num))
        file.write("Address: " + address)
        file.write("Purchased Date: " + day + "/" + month + "/" + year )
            #details of purchased items in the invoice
            
        file.write("S.N \t Product Name \t\t Purchased Quantity \t\t Rate \t\tTotal Price")

        if type_of_transaction == "purchase":
            serial_number = 1
            total = 0 + ship_price
            for values in purchased_item_list:
                    
                    #details of purchased item to the invoice.
                    
                file.write(str(serial_number)+" " + str( values[0])+ " " + str( values[1])+ " " + str(values[2])+ " " + str(values[3]))

                    #increment the serial_number variable
                serial_number+= 1

                    #adding the item's price to the total variable
                total += int(values[3])

                #if no shipping cost, add final total to the invoice
            if ship_price == 0:
                file.write("Final Total : " + str(total))

                #if shipping cost ,  add shipping cost and total amount to invoice  
            else:
                file.write("Shipping Cost : "+ str( ship_price) )
                file.write("Total Amount: " + str(total) )
            

            #if transaction type return, shipping cost is not added to the total

        else:
            serial_number = 1
            total = 0
            for values in purchased_item_list:

                    #writting details of purchased item to the invoice
                file.write(str(serial_number) +"\t"+ str(values[0])+"\t"+ str(values[1])+"\t\t"+ str(values[2])+"\t\t"+ str(values[3]))
            

                    #increments serial_number variable
                serial_number += 1

                    #adds item price to the total variable
                total += values[3]
                

                #calculates amount after VAT and the total cost after VAT
            amount_after_vat = total_cost * (13/100)
            totalcost_after_vat = amount_after_vat + total


                #writes total cost, amount after vat, and total cost after VAT
            file.write("Total: " +str(total))
            file.write("Amount when vat added: " +str(amount_after_vat))
            file.write("Total cost after VAT added :  "+ str(totalcost_after_vat))
        file.close()
            
"""
