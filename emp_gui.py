import tkinter as tk
from var import *

def add_employee_gui():
    #win.mainloop()
    if  not (username and password and role and emp_id and name and age and gender and place and salary and pre_company and join_date):
        print("Cannot add employee without all details. Try again")
    else:
        if emp_id.get() in employees.keys():
            print("Employee id already exists. Cannot add employee")
        else:
            employees[emp_id.get()] = Employee(username.get(), password.get(), role.get(), emp_id.get(), name.get(), age.get(), gender.get(), place.get(), salary.get(), pre_company.get(), join_date.get())
            #reset_add_employee_gui()
            fr_username.delete(0, 'end')
            fr_password.delete(0, 'end')
            fr_role.delete(0, 'end')
            fr_emp_id.delete(0, 'end')
            fr_name.delete(0, 'end')
            fr_age.delete(0, 'end')
            fr_gender.delete(0, 'end')
            fr_place.delete(0, 'end')
            fr_salary.delete(0, 'end')
            fr_pre_company.delete(0, 'end')
            fr_join_date.delete(0, 'end')
            msg.set("Employee Added")
            lst.delete(0,'end')
            

def display_employee_gui():
    for emp_id, employee in employees.items():
        lst.insert(tk.END, employee.name)


# Creating Window for adding employee
win = tk.Tk()
win.title("Employee Entry")
win.geometry("600x400")

l_frame = tk.Frame(win)
l_frame.grid(row = 0, column = 0)
r_frame = tk.Frame(win)
r_frame.grid(row = 0, column = 1)

# Creating variables
username = tk.StringVar(l_frame)
password = tk.StringVar(l_frame)
role = tk.StringVar(l_frame)
emp_id = tk.StringVar(l_frame)
name = tk.StringVar(l_frame)
age = tk.StringVar(l_frame)
gender = tk.StringVar(l_frame)
place = tk.StringVar(l_frame)
salary = tk.StringVar(l_frame)
pre_company = tk.StringVar(l_frame)
join_date = tk.StringVar(l_frame)
msg  = tk.StringVar(l_frame)

tk.Label(l_frame,text = "Username").grid(row=0,column=0)
fr_username = tk.Entry(l_frame,textvariable=username)
fr_username.grid(row=0,column=1)

tk.Label(l_frame,text = "Password").grid(row=1,column=0)
fr_password = tk.Entry(l_frame,textvariable=password)
fr_password.grid(row=1,column=1)

tk.Label(l_frame,text = "Role").grid(row=2,column=0)
fr_role = tk.Entry(l_frame,textvariable=role)
fr_role.grid(row=2,column=1)

tk.Label(l_frame,text = "Employee ID").grid(row=3,column=0)
fr_emp_id = tk.Entry(l_frame,textvariable=emp_id)
fr_emp_id.grid(row=3,column=1)

tk.Label(l_frame,text = "Name").grid(row=4,column=0)
fr_name = tk.Entry(l_frame,textvariable=name)
fr_name.grid(row=4,column=1)

tk.Label(l_frame,text = "Age").grid(row=5,column=0)
fr_age = tk.Entry(l_frame,textvariable=age)
fr_age.grid(row=5,column=1)

tk.Label(l_frame,text ="Gender").grid(row=6,column=0)
fr_gender = tk.Entry(l_frame,textvariable=gender)
fr_gender.grid(row=6,column=1)

tk.Label(l_frame,text = "Salary").grid(row=7,column=0)
fr_salary = tk.Entry(l_frame,textvariable=salary)
fr_salary.grid(row=7,column=1)

tk.Label(l_frame,text = "Place").grid(row=8,column=0)
fr_place = tk.Entry(l_frame,textvariable=place)
fr_place.grid(row=8,column=1)

tk.Label(l_frame,text = "Joining Date").grid(row=9,column=0)
fr_join_date = tk.Entry(l_frame,textvariable=join_date)
fr_join_date.grid(row=9,column=1)

tk.Label(l_frame,text = "Previous Company").grid(row=10,column=0)
fr_pre_company = tk.Entry(l_frame,textvariable=pre_company)
fr_pre_company.grid(row=10,column=1)

tk.Button(l_frame,text="Submit",command = add_employee_gui).grid(row=15,column=0)
tk.Button(l_frame,text="Display",command = display_employee_gui).grid(row=15,column=1)

fr_msg = tk.Label(r_frame,textvariable=msg)
fr_msg.grid(row=25,column=1)

lst=tk.Listbox(r_frame)
lst.grid(row=0,column=1)
