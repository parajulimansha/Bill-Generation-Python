"""This program reads laptop details from a text file, 'laptop.txt' , and displays them on a console.
            The 'reading_laptop()' function reads the contents of the file and creates a dictionary of laptop detals    
            with laptop ID's as the keys and a list of laptop properties as the values."""
                                                                                        
laptop_details = {}
def read_laptop_details() :
    
    with open("laptop.txt","r") as file: #opens "laptop.txt" file in read mode using with statement
        laptop_id =1 #initializes laptop ID to 1
        for line in file: #iterates through each line in the file
            line = line.strip()  #removes new line character( any white space from the lne)
            laptop_details[laptop_id] = line.split(",") #splite the line by comma and adds the result as a value for the laptop ID key in the dictionary
            laptop_id += 1 #increments the laptop ID for the next iteration
    return laptop_details # returns the dictionary of laptop details

""" The 'display_laptop_details()' function reads the contents of the file and displays the laptop details in a tabular ormat on the console.
The laptop details include the serial number, laptop name, company name,
            price, quantity, processor, and graphics card."""
                                                          

def display_laptop_details():
    with open("laptop.txt","r") as file: # opens the "laptop.txt" file in read mode using 'with' statement
        details = file.readlines() #reads all lines of the file and returns a list of strings, where each string represents a line
    print("-" * 120) #prints a horizontal line using '-' character
    print("S.N \t Laptop Name \t\t Company Name \t\t Price \t\t Quantity \t Processor \t Graphics Card") # prints the header row for the table for the table of laptop details
    print("-" * 120)
    
    serial_num = 1  #serial nummber is used as a counter here to keep track of the index of current lne being processed in for loop
    for line in details: #iterates through each line in the details list
        print(serial_num, "\t" , line.replace(",","\t\t")) #prints the serial number followed by line contents
        serial_num += 1 # increments the serial number for the next iteration


""" We are using while loop to iterate over the ile in 'read_laptop_details()', and
            manually increment 'laptop_id'. The 'display_laptop_details()', seperate 'serial_num'
            variable is initialised to 1, and then it is manually incremented for each line in the file
            Both unctions use the 'with' statement to automatically close the file after reading from it. """                                                                                           

