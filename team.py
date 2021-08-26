from var import *
from employee import display_employee


def manage_teams_menu():
    print("\n\t1. Create new team")
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
    print("\n\t\t1. Add employee")
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

