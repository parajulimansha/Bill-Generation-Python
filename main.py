import read
import operations

#introducing the store
print("-"*120,"\n")
print("-"*50 , "Mansha Electroincs" , "-"*47 , "\n \n")
print("-"*50 , "Welcome to out store" , "-"*47 , "\n""\n")
print("-"*40 , "Buy anything you want in wholesale price" , "-"*40 , "\n")

select = True

while select:
    print("Select 1 for selling the products to the customers ")
    print("Select 2 for buying the items from the manufacturers ")
    print("Select 3 to Exit from the Server ")


    try:
        user_select = int(input("Select a number to use the server : "))

        if user_select == 1:
            operations.products_for_selling()
           

        elif user_select == 2:
            operations.products_for_purchase()
           

        elif user_select == 3:
            print("Thank you for visiting our store !! \nHope to see you again!!")
            select = False

        else:
            print("The option can only be selected from 1, 2, and 3.\nPlease try inserting valid choices")

    except:
        print("Error found please try again later!!\n\n")

   
        

