from var import *

def search_employee_menu():
    print("\n\t1. Search employee by name")
    print("\t2. Search employee by age")
    print("\t3. Search employee by salary")
    print("\t4. Search employee by gender")
    print("\t5. Return to previous menu")


def search_employee_by_name():
    name = input("\tEnter employee name: ")
    emp_present = False
    if name:
        for emp_id, employee in employees.items():
            if employee["name"] == name:
                emp_present = True
                print(f"\n\tEmployee id: \t {emp_id}")
                for key in employee:
                    print(f"\t{key}: \t {employee[key]}")
        if not emp_present:
            print("\t" + name + " is not an employee.")

    else:
        print("\tNo valid input received. Try again")


def search_employee_by_age():
    age = input("\tEnter employee age: ")
    emp_present = False
    if age:
        for emp_id, employee in employees.items():
            if employee["age"] == age:
                emp_present = True
                print(f"\n\tEmployee id: \t {emp_id}")
                for key in employee:
                    print(f"\t{key}: \t {employee[key]}")
        if not emp_present:
            print("\t" + age + " is not an age of any employee.")

    else:
        print("\tNo valid input received. Try again")


def search_employee_by_salary():
    salary = input("\tEnter employee salary: ")
    emp_present = False
    if salary:
        for emp_id, employee in employees.items():
            if employee["salary"] == salary:
                emp_present = True
                print(f"\n\tEmployee id: \t {emp_id}")
                for key in employee:
                    print(f"\t{key}: \t {employee[key]}")
        if not emp_present:
            print("\t" + salary + " is not salary of any employee.")

    else:
        print("\tNo valid input received. Try again")


def search_employee_by_gender():
    gender = input("\tEnter employee gender: ")
    emp_present = False
    if gender:
        for emp_id, employee in employees.items():
            if employee["gender"] == gender:
                emp_present = True
                print(f"\n\tEmployee id: \t {emp_id}")
                for key in employee:
                    print(f"\t{key}: \t {employee[key]}")
        if not emp_present:
            print("\t" + gender + " is not gender of any employee.")

    else:
        print("\tNo valid input received. Try again")


def search_employee():
    while True:
        search_employee_menu()
        ch = input("\tEnter your choice: ")
        if ch == '1':
            # Search employee by name
            search_employee_by_name()

        elif ch == '2':
            # Search employee by age
            search_employee_by_age()

        elif ch == '3':
            # Search employee by salary
            search_employee_by_salary()

        elif ch == '4':
            # Search employee by gender
            search_employee_by_gender()

        elif ch == '5':
            # Exit
            break

        else:
            print("\tInvalid choice!!!")