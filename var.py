employees = {} # Dict for employee details
org = {} # Dict for organization details
teams = {} # Dict for employees team details

class Employee:
	def __init__(self, emp_id, name, age, gender, place, salary, previous_company, join_date):
		self.emp_id = emp_id
		self.name = name
		self.age = age
		self.gender = gender
		self.place = place
		self.salary = salary
		self.previous_company = previous_company
		self.join_date = join_date

	def set_emp_id(self, emp_id):
		self.emp_id = emp_id

	def set_name(self, name):
		self.name = name

	def set_age(self, age):
		self. age = age

	def set_gender(self, gender):
		self.gender = gender

	def set_place(self, place):
		self.place = place

	def set_salary(self, salary):
		self.salary = salary

	def set_previous_company(self, previous_company):
		self.previous_company = previous_company

	def set_join_date(self, join_date):
		self.join_date = join_date
