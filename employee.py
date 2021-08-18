employees = {} # Dict for employee details
teams = {} # Dict for employees team details
org = {} # Dict for organization details


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

            #Delete the emp_id from teams
            for team_name, emp_lst in teams.items():
                if emp_id in emp_lst:
                    teams[team_name].remove(emp_id)
                    print(f"Deleted {emp_id} : {name} from {team_name}")

        else:
            print(emp_id+" is not an existing employee id. Cannot delete.")
    else:
        print("No valid input received. Try again")


def search_employee_by_name():
    name = input("Enter employee name: ")
    emp_present = False
    if name:
        for emp_id, employee in employees.items():
            if employee["name"] == name:
                emp_present = True
                print(f"\tEmployee id: \t {emp_id}")
                for key in employee:
                    print(f"\t{key}: \t {employee[key]}")
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


def manage_teams_menu():
    print("\t1. Create new team")
    print("\t2. Display team")
    print("\t3. Manage particular team")
    print("\t4. Delete team")
    print("\t5. Return to previous menu")


def create_new_team():
    team_name = input("\tEnter team name: ")
    teams[team_name] = []

def display_teams():
        
    for team_name,emp_lst in teams.items():

        name_string = ""
        #Print data
        for emp_id in emp_lst:  #For each employee id in the particular team
            name_string = f"{name_string} | {emp_id}. {employees[emp_id]['name']}"
        
        print(f"{team_name} => {name_string}")



def manage_particular_team_menu():
    print("\t\t1. Add employee")
    print("\t\t2. Delete employee")
    print("\t\t3. List employee")
    print("\t\t4. Rename team")
    print("\t\t5. Go to previous menu")


def add_employee_to_team(team_name):
    display_employee()
    emp_id = input("\t\tEnter employee id: ")

    if emp_id in employees.keys() and team_name in teams:
        teams[team_name].append(emp_id)
    else:
        print("\t\tWrong employee id")


def delete_employee_from_team(team_name):
    list_employees_in_team(team_name)

    emp_id = input("\t\tEnter the employee id of the employee to be removed from team: ")
    if emp_id in teams[team_name]:
        teams[team_name].remove(emp_id)
    else:
        print("\t\tWrong employee id.")


def list_employees_in_team(team_name):
    name_string = ""

    if team_name in teams.keys():
        #Print data
        
        for emp_id in teams[team_name]:  #For each employee id in the particular team
            name_string = f"{name_string} | {emp_id}. {employees[emp_id]['name']}"
    
    print(name_string)


def rename_team(team_name):
    display_teams()
    if team_name in teams.keys():
        new_name = input("\t\tEnter new team_name: ")
        teams[new_name] = teams[team_name]
        del teams[team_name]
    else:
        print("\t\tWrong team name. Doesn't exist")


def manage_particular_team():
    
    while True:
        
        manage_particular_team_menu()
        ch = input("\t\tEnter your choice: ")
        if ch and ch != '5':
            team_name = input("\t\tEnter the team name: ")

        if ch == '1':
            #Add employee
            add_employee_to_team(team_name)

        elif ch == '2':
            #Delete employee
            delete_employee_from_team(team_name)

        elif ch == '3':
            #List employee
            list_employees_in_team(team_name)

        elif ch == '4':
            #Rename team
            rename_team(team_name)

        elif ch == '5':
            break


def delete_team():
    team_name = input("\t\tEnter the team name: ")
    if team_name in teams.keys():
        del teams[team_name]
        print(f"\t\t Deleted the team {team_name}")
    else:
        print("\t\tWrong team name. Doesn't exist.")


def manage_teams():
    while True:
        manage_teams_menu()
        ch = input("Enter your choice: ")
        if ch:
            if ch == '1':
                #Create new team
                create_new_team()

            elif ch == '2':
                #Display team
                display_teams()

            elif ch == '3':
                #Manage particular team
                manage_particular_team()

            elif ch == '4':
                #Delete team
                delete_team()
            
            elif ch == '5':
                #Return to previous menu
                break


def add_organization():
    name = input("Enter organization name: ")
    email = input("Enter organization email: ")
    if name and email:
        org["name"] = name
        org["email"] = email
    else:
        print("Cannot leave name or email empty. Try again.")


def manage_organization_menu():
    print("\t1. Change organization name")
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




# Add organization on first setup
add_organization()
while True:
    
    print_main_menu()

    choice = input("Enter your choice: ")
    if not choice:
        print("Enter a valid number from 1 to 7.")
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
        search_employee_by_name()
    
    elif choice == 4:
        # Change employee Data
        change_employee_data()
               
    elif choice == 5:
        # Display Employees
        display_employee()

    elif choice == 6:
        #Manage Teams
        manage_teams()

    elif choice == 7:
        #Manage organization
        manage_organization()
        
    elif choice == 8:
        # Exit
        break
    else:
        print("Invalid entry!! Choose number from 1-6")

