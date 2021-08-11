
employee = []
while True:
    print("\n\n_________MENU_________")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. Change Employee Data")
    print("5. Display Employees")
    print("6. Exit")

    choice = int(input())

    if choice == 1:
        # Add Employee
        name = input("Enter employee name: ")
        if name:
            employee.append(name)
            print("Added " +name+ " to employees")
        else:
            print("No valid input received. Try again")

    elif choice == 2:
        # Delete Employee
        print("Existing Employees\n", employee)
        name = input("Enter employee name to be deleted: ")
        if name:
            if name in employee:
                employee.remove(name)
                print("Deleted " +name+ " from employees")
            else:
                print(name+" is not an employee. Cannot delete.")
        else:
            print("No valid input received. Try again")

    elif choice == 3:
        #Search Employee
        name = input("Enter employee name: ")
        if name:
            if name in employee:
                print(name + " is an employee.")
            else:
                print(name + " is not an employee.")

        else:
            print("No valid input received. Try again")

    elif choice == 4:
        # Change employee Data
        name = input("Enter employee name: ")
        if name:
            if name in employee:
                indx = employee.index(name)
                new_name = input("Enter the new name: ")
                if new_name:
                    employee[indx] = new_name
                    print("Changed the name " + name + "to" + new_name)
                else:
                    print("No valid input received. Cannot change employee data.")
            else:
                print(name + " is not an employee.")

        else:
            print("No valid input received. Try again")

    elif choice == 5:
        # Display Employees
        i = 1
        for emp in employee:
            print(str(i) + ". "+ emp)
            i  +=1

    elif choice == 6:
        # Exit
        break
    else:
        print("Invalid entry!! Choos number from 1-6")

