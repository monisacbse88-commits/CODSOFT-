#Create empty list to store contact details
contact_book=[]

#Function to add contacts
def add_contact():
    name=input("Enter name:")
    phone_number=input("Enter 10 digit phone number:")
    email=input("Enter valid email id:")
    address=input("Enter address of contact:")
    contact_book.append({'Name':name,'Phone number':phone_number,'Email':email,'Address':address})
    print("Contact added successfully!!!")

#Function to view all contacts
def view_contacts():
    print("****Contact Book****")
    if len(contact_book)==0:
        print("No available contact details")
    for index,contact in enumerate(contact_book,1):
        print(f"{index}.Name:{contact['Name']}\tPhone number:{contact['Phone number']}\tEmail:{contact['Email']}\tAddress:{contact['Address']}")
    print("\n")

#Function to search by name
def search_by_name():
    search_name=input("Enter name to be searched:")
    found=0
    if len(contact_book)==0:
        print("No available contact details")
    for index,contact in enumerate(contact_book,1):
        if contact['Name'].lower()==search_name.lower():
            found=1
            print(f"{index}.Name:{contact['Name']}\tPhone number:{contact['Phone number']} \tEmail:{contact['Email']} \tAddress:{contact['Address']}")
    if found!=1:
        print("No related results for given name")
    print("\n")   

#Function to search by phone number
def search_by_number():
    search_number=input("Enter number to be searched:")
    found=0
    if len(contact_book)==0:
        print("No available contact details")
    for index,contact in enumerate(contact_book,1):
        if contact['Phone number']==search_number:
            print(f"{index}.Name:{contact['Name']}\tPhone number:{contact['Phone number']}\tEmail:{contact['Email']}\tAddress:{contact['Address']}")
            found=1
    if found!=1:
        print("No related results for given number")    
    print("\n")   

#Function to update contact details
def update_contacts():
    view_contacts()
    contact_number=int(input("Enter contact number to be updated:"))-1
    if contact_number>=0 and contact_number<len(contact_book):
        print(contact_book[contact_number])
        while True:
            key=input("Enter Detail to be updated(Name/Phone number/Email/Address):")
            contact_book[contact_number][key]=input("Enter new contact detail:")
            c=input("Do you want to continue(y/n):")
            if c=='n':
                break
    else:
        print("Invalid contact number")

#Function to delete contact
def delete_contact():
    view_contacts()
    contact_number=int(input("Enter contact number to be deleted:"))-1
    if contact_number>=0 and contact_number<len(contact_book):
        deleted_contact=contact_book.pop(contact_number)
        print(f"Removed contact:{deleted_contact}")
    else:
        print("Invalid contact number")

#Menu function
def menu():
    while True:
        print("Operations:\n\
               1. Add a new contact.\n\
               2. View all contacts with names and phone numbers.\n\
               3. Search contacts by name or phone number.\n\
               4. Update contact details.\n\
               5. Delete a contact\n\
               6. Exit application.")
        choice=int(input("Enter your choice of operation:"))
        if choice==1:
            add_contact()
        elif choice==2:
            view_contacts()
        elif choice==3:
            print("Enter 1 to search by name or 2 to search by phone number:")
            c=int(input("Enter choice:"))
            if c==1:
                search_by_name()
            elif c==2:
                search_by_number()
            else:
                print("Invalid!!!")
        elif choice==4:
            update_contacts()
        elif choice==5:
            delete_contact()
        elif choice==6:
            print("Exiting application....")
            exit()
        else:
            print("Invalid choice!! Try again")

menu()
