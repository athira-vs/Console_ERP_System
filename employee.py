def print_main_menu():
    print("\n\n_________MENU_________")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. Change Employee Data")
    print("5. Display Employees")
    print("6. Exit")

def add_employee():
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


def delete_employee():
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


def search_employee():
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


def display_employee():
    for emp_id, employee in employees.items():
        print(f"\n\tEmployee id: \t {emp_id}")
        for key in employee:
            print(f"\t{key} \t {employee[key]}")


def change_employee_menu():
    print("\tMENU")
    print("\t1. Change employee name")
    print("\t2. Change age")
    print("\t3. Change gender")
    print("\t4. Change place")
    print("\t5. Change salary")
    print("\t6. Change previous company")
    print("\t7. Change joining date")
    print("\t8. Return to main menu")


def change_joining_date(emp_id):
    join_date = input("Enter new joining date: ")
    if join_date:
        employees[emp_id]["join_date"] = join_date
    else:
        print("No valid input received. Cannot change employee data.")


def change_previous_company(emp_id):
    pre_company = input("Enter previous company: ")
    if pre_company:
        employees[emp_id]["previous_company"] = pre_company
    else:
        print("No valid input received. Cannot change employee data.")


def change_salary(emp_id):
    salary = input("Enter new employee salary: ")
    if salary:
        employees[emp_id]["salary"] = salary
    else:
        print("No valid input received. Cannot change employee data.")


def change_employee_place(emp_id):
    place = input("Enter new employee place: ")
    if place:
        employees[emp_id]["place"] = place
    else:
        print("No valid input received. Cannot change employee data.")


def change_employee_gender(emp_id):
    gender = input("Enter new employee gender: ")
    if gender:
        employees[emp_id]["gender"] = gender
    else:
        print("No valid input received. Cannot change employee data.")


def change_employee_age(emp_id):
    age = input("Enter new employee age: ")
    if age:
        employees[emp_id]["age"] = age
    else:
        print("No valid input received. Cannot change employee data.")


def change_employee_name(emp_id):
    name = input("Enter new employee name: ")
    if name:
        employees[emp_id]["name"] = name
    else:
        print("No valid input received. Cannot change employee data.")


def change_employee_data():
    while True:
        emp_id = input("Enter employee id to be changed: ")
        if not emp_id:
            print("No valid input received. Try again")
        else:
            if emp_id in employees.keys():

                change_employee_menu()
                ch = input("\tEnter your choice: ")

                if not ch:
                    print("Enter a valid number from 1 to 8.")
                    continue
                else:
                    ch = int(ch)
                    if ch == 1:
                        #Change employee name
                        change_employee_name(emp_id)
                    elif ch == 2:
                        #Change age
                        change_employee_age(emp_id)

                    elif ch == 3:
                        #Change gender
                        change_employee_gender(emp_id)

                    elif ch == 4:
                        #Change place
                        change_employee_place(emp_id)

                    elif ch == 5:
                        #Change salary
                        change_salary(emp_id)

                    elif ch == 6:
                        #Change previous company
                        change_previous_company(emp_id)

                    elif ch == 7:
                        #Change joining date
                        change_joining_date(emp_id)

                    elif ch == 8:
                        #Return to main menu
                        break

                    else:
                        print("\tInvalid choice.")
                    
            else:
                print(emp_id+" is not an existing employee id. Cannot modify.")


employees = {}
while True:
    print_main_menu()

    choice = input()
    if not choice:
        print("Enter a valid number from 1 to 6.")
        continue
    else:
        choice = int(choice)
    if choice == 1:
        # Add Employee
        add_employee()
        
        
    elif choice == 2:
        # Delete Employee
        #print("Existing Employees\n", employee)
        delete_employee()

    elif choice == 3:
        #Search Employee
        search_employee()
    
    elif choice == 4:
        # Change employee Data
        change_employee_data()
               
    elif choice == 5:
        # Display Employees
        display_employee()
        
    elif choice == 6:
        # Exit
        break
    else:
        print("Invalid entry!! Choose number from 1-6")

