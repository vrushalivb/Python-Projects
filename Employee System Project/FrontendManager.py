from EmployeeManager import *

class FrontendManager:
  # creating an object of EmployeeManager and storing into self.manager(to access all the functions of EmployeeManager into this class)
  def __init__(self):
    self.manager = EmployeeManager()

#  showing Menu
  def print_menu(self):
    print("\n-----Employee System Menu-----")
    print("1) Add New Employee")
    print("2) Show All Employees")
    print("3) Delete Employees Based on Age Range")
    print("4) Update Employees salaries by Name")
    print("5) End Program")

  def execute(self):
    while True:
      self.print_menu()
      choice = int(input("Enter your choice between (1-5) : "))

      # add new employee
      if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        self.manager.add_employee(name, age, salary)
        print("\nEmployee Added Successfully")

      # show all employees
      elif choice == 2:
        self.manager.list_employees()

      # delete employee between age range
      elif choice == 3:
        min_age = int(input("Enter Minimum starting age : "))
        max_age = int(input("Enter Maximum ending age : "))
        self.manager.delete_employees_by_age(min_age, max_age)


      # update employee salary by name
      elif choice == 4:
        name = input("Enter Name : ")
        salary = float(input("Enter New Salary : "))
        self.manager.update_salary(name, salary)
        print("\nSalary Updated successfully! ")

      # exit system
      elif choice == 5:
        break

      else:
        print("Invalid Choice! Try again.")