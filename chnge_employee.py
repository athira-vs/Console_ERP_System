from var import *

def change_employee_menu():
    print("\n\tMENU")
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
