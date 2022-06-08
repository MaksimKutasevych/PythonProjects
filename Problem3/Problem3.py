from database import Database
from prettytable import PrettyTable
import sqlite3

#Checking database if it's not empty
def checkdatabase():
    if db.get_contacts():
        return True
    else:
        return False

#Printing contacts table
def printcontacts():

    contacts = db.get_contacts()

    print("\nAll Contacts:")

    t = PrettyTable(['Number','Name','Address','Email'])

    for contact in contacts:
        (number, name, address, email) = contact
        t.add_row([number, name, address, email])


    print(t)

#Creating contact
def createcontact():
    return data_input(is_creating=True)

#Deleting contact
def deletecontact():
    printcontacts()

    while True:
        number = input("Enter the number of contact you want to delete: ")

        #Cheching input
        if number.isdigit():

            #Checking if contact info is in the DataBase
            if db.is_number_in_base(number):
                db.delete_contact(number)
                print("Contact Deleted!")
                printcontacts()
                break

        else:
            print("Incorrect input, try again!")

#Update contact info
def updatecontact():
    printcontacts()

    while True:
        number = input("Enter the number of contact you want to update: ")

        # Cheching input
        if number.isdigit():

            # Checking if contact info is in the DataBase
            if db.is_number_in_base(number):
                db.update_contact(number,*data_input())
                print("Contact updated!")
                printcontacts()
                break

            else:
                print("There's no such number in base!")


        else:
            print("Incorrect input, try again!")




def data_input(is_creating=False):
    while True:

        number = input("Input number: ")
        # Cheching input
        if number.isdigit():

            # Cheching if we create new contact or just update it's info
            if is_creating:

                # Checking if contact info is in the DataBase
                if db.is_number_in_base(number):
                    print("There is such number in base, try again!")
                    continue

            break

        else:
            print("Number must be a number!")

    #Data inputs with input checks
    while True:
        name = input("Input name: ")
        if name.isalpha():
            break
        print("Name must be a letters!")

    while True:
        address = input("Input address: ")
        if address.strip() != '':
            break
        print("Address can't be empty!")

    email = input("Input email: ")

    return (number, name, address, email)






try:

    #Connecting to DB
    db = Database("contactsbook.db")

    print("It's contact book!")

    while True:

        print("\nChoose an option:")

        #If DB is not empry
        if checkdatabase():

            #Menu
            print("1 Show all contacts\n2 Create contact\n3 Delete contact\n4 Update contact information\n5 Exit")

            #Choice input check
            while True:
                choice = input("Your choice? ")
                if choice.isdigit() and int(choice) > 0 and int(choice) < 6:
                    break
                else:
                    print("Incorrect input, try again!")

            #Different choices and actions
            if int(choice) == 1:
                printcontacts()
            elif int(choice) == 2:
                (number, name, address, email) = createcontact()
                db.add_contact(number,name,address,email)
                printcontacts()
            elif int(choice) == 3:
                deletecontact()
            elif int(choice) == 4:
                updatecontact()
            elif int(choice) == 5:
                break

        #If DB is empry
        else:
            print("1 Create contact\n2 Exit")

            while True:
                choice = input("Your choice? ")
                if choice.isdigit() and int(choice) > 0 and int(choice) < 3:
                    break
                print("Incorrect input, try again!")


            if int(choice) == 1:
                (number, name, address, email) = createcontact()
                db.add_contact(number, name, address, email)
                printcontacts()

            elif int(choice) == 2:
                break


finally:
    db.close_connection()
