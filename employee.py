
employees = {}
while True:
    print("\n\n_________MENU_________")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. Change Employee Data")
    print("5. Display Employees")
    print("6. Exit")

    choice = input()
    if not choice:
        print("Enter a valid number from 1 to 6.")
        continue
    else:
        choice = int(choice)
    if choice == 1:
        # Add Employee
        emp_id = input("Enter employee id: ")
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        gender = input("Enter employee gender: ")
        place = input("Enter employee place: ")
        salary = input("Enter employee salary: ")
        pre_company = input("Enter previous company: ")
        join_date = input("Enter joining date: ")
        
        if  not (emp_id and name and age and gender and place and salary and pre_company and join_date):
            print("Cannot add employee without all details. Try again")
        else:
            if emp_id in employees.keys():
                print("Employee id already exists. Cannot add employee")
            else:
                temp = {}
                temp["name"] = name
                temp["age"] = age
                temp["gender"] = gender
                temp["place"] = place
                temp["salary"] = salary
                temp["previous_company"] = pre_company
                temp["join_date"] = join_date

                employees[emp_id] = temp

                print("Added " +name+ " to employees")
        
    elif choice == 2:
        # Delete Employee
        #print("Existing Employees\n", employee)
        emp_id = input("Enter employee id to be deleted: ")
        if emp_id:
            if emp_id in employees.keys():
                name = employees[emp_id]["name"]
                del employees[emp_id]
                print(f"Deleted {emp_id} : {name} from employees")
            else:
                print(emp_id+" is not an existing employee id. Cannot delete.")
        else:
            print("No valid input received. Try again")

    elif choice == 3:
        #Search Employee
        name = input("Enter employee name: ")
        emp_present = False
        if name:
            for emp_id, employee in employees.items():
                if employee["name"] == name:
                    emp_present = True
                    print(f"\tEmployee id: \t\t {emp_id}")
                    for key in employee:
                        print(f"\t{key}: \t\t {employee[key]}")
            if not emp_present:
                print(name + " is not an employee.")

        else:
            print("No valid input received. Try again")
    
    elif choice == 4:
        # Change employee Data
        
        emp_id = input("Enter employee id to be changed: ")
        if not emp_id:
            print("No valid input received. Try again")
        else:
            if emp_id in employees.keys():

                print("\tMENU")
                print("\t1. Change employee name")
                print("\t2. Change age")
                print("\t3. Change gender")
                print("\t4. Change place")
                print("\t5. Change salary")
                print("\t6. Change previous company")
                print("\t7. Change joining date")
                ch = input("\tEnter your choice: ")
                if not ch:
                    print("Enter a valid number from 1 to 7.")
                    continue
                else:
                    ch = int(ch)
                    if ch == 1:
                        name = input("Enter new employee name: ")
                        if name:
                            employees[emp_id]["name"] = name
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 2:
                        age = input("Enter new employee age: ")
                        if age:
                            employees[emp_id]["age"] = age
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 3:
                        gender = input("Enter new employee gender: ")
                        if gender:
                            employees[emp_id]["gender"] = gender
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 4:
                        place = input("Enter new employee place: ")
                        if place:
                            employees[emp_id]["place"] = place
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 5:
                        salary = input("Enter new employee salary: ")
                        if salary:
                            employees[emp_id]["salary"] = salary
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 6:
                        pre_company = input("Enter previous company: ")
                        if pre_company:
                            employees[emp_id]["previous_company"] = pre_company
                        else:
                            print("No valid input received. Cannot change employee data.")
                    elif ch == 7:
                        join_date = input("Enter new joining date: ")
                        if join_date:
                            employees[emp_id]["join_date"] = join_date
                        else:
                            print("No valid input received. Cannot change employee data.")
                    else:
                        print("\tInvalid choice.")
            else:
                print(emp_id+" is not an existing employee id. Cannot modify.")
   
    elif choice == 5:
        # Display Employees
        for emp_id, employee in employees.items():
            print(f"\n\tEmployee id: \t {emp_id}")
            for key in employee:
                print(f"\t{key} \t {employee[key]}")
        

    elif choice == 6:
        # Exit
        break
    else:
        print("Invalid entry!! Choos number from 1-6")

