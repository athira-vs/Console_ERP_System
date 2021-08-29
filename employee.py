from var import *

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
            temp = Employee(emp_id, name, age, gender, place, salary, pre_company, join_date)
            '''
            temp.name = name
            temp.age = age
            temp.gender = gender
            temp.place = place
            temp.salary = salary
            temp.previous_company = pre_company
            temp.join_date = join_date
            '''
            employees[emp_id] = temp

            print("Added " +name+ " to employees")


def delete_employee():
    emp_id = input("Enter employee id to be deleted: ")
    if emp_id:
        if emp_id in employees.keys():
            name = employees[emp_id].name
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


def display_employee():
    for emp_id, employee in employees.items():
        print("\n")
        key_list = employee.__dict__.keys()
        for key in key_list:
            print(f"\t{key} \t {getattr(employee, key)}")


