from var import *

def add_organization():
    name = input("Enter organization name: ")
    email = input("Enter organization email: ")
    if name and email:
        org["name"] = name
        org["email"] = email
    else:
        print("Cannot leave name or email empty. Try again.")


def manage_organization_menu():
    print("\n\t1. Change organization name")
    print("\t2. Change organization email")
    print("\t3. Display organization")
    print("\t4. Return to previous menu")


def change_org_name():
    new_name = input("Enter new organization name: ")
    if new_name:
        org["name"] = new_name
    else:
        print("Cannot leave name empty. Try again.")


def change_org_email():
    new_email = input("Enter new organization email: ")
    if new_email:
        org["email"] = new_email
    else:
        print("Cannot leave email empty. Try again.")

def display_organization():
    for key, value in org.items():
        print("\t{} => {}".format(key,value))



def manage_organization():
    while True:
        manage_organization_menu()
        ch = input("Enter your choice: ")
        if ch == '1':
            # Change organization name
            change_org_name()        

        elif ch == '2':
            # Change organization email
            change_org_email()

        elif ch == '3':
            # Dispaly organization
            display_organization()

        elif ch == '4':
            # Exit
            break

        else:
            print("Invalid choice!!!")

