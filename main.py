import organization as orgn
import team as tm
import employee as em
import srch_employee as srch_em
import chnge_employee as ch_em


def print_main_menu():
    print("\n\n_________MENU_________")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. Change Employee Data")
    print("5. Display Employees")
    print("6. Manage Teams")
    print("7. Manage organization")
    print("8. Exit")


# Add organization on first setup
orgn.add_organization()
while True:
    
    print_main_menu()

    choice = input("Enter your choice: ")
    if not choice:
        print("Enter a valid number from 1 to 8.")
        continue
    else:
        choice = int(choice)
    if choice == 1:
        # Add Employee
        em.add_employee()
        
        
    elif choice == 2:
        # Delete Employee
        #print("Existing Employees\n", employee)
        em.delete_employee()

    elif choice == 3:
        #Search Employee
        srch_em.search_employee()
    
    elif choice == 4:
        # Change employee Data
        ch_em.change_employee_data()
               
    elif choice == 5:
        # Display Employees
        em.display_employee()

    elif choice == 6:
        #Manage Teams
        tm.manage_teams()

    elif choice == 7:
        #Manage organization
        orgn.manage_organization()
        
    elif choice == 8:
        # Exit
        break
    else:
        print("Invalid entry!! Choose number from 1-8")

