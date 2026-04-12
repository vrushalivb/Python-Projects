from Employee import *

class EmployeeManager:
  def __init__(self):
    self.employees = []

 # • adding employees details to the list
  def add_employee(self, name, age, salary):
    self.employees.append(Employee(name, age, salary))


 # • list all existing employees
  def list_employees(self):

    # checking if there are no employees
    if not self.employees:
      # if no employees printing this statement
      print("\n No employees found")
     #if no employees found function stops
      return

      # if employees found below statement will execute
    print("\n--- Current Employee List ---")
    # iterating one by one employees and printing it
    for emp in self.employees:
      print(emp)



  # • Delete employees within a specified age range.
  def delete_employees_by_age(self, min_age, max_age):

    #storing current employee count
    cur_emp_count = len(self.employees)

    # iterating employees one by one
    # keeps employees which are not in range
    # overwrites the old list with new (after deleted)
    self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    # just showing count how many employees removed
    print(f"\nRemoved {cur_emp_count - len(self.employees)} employees.")


#  • Find an employee by their name.
  def find_employee_by_name(self, name):
    # checking one by one employee names
    for emp in self.employees:
      # if name from list and entered name is same
      if emp.name.lower() == name.lower():
        # returns name
        return emp

    # if emplyoee name didn't find
    return f"There is no employee with name {name}"


# • Update an employee's salary by name.
  def update_salary(self, name, new_salary):
      # checking name is there
        emp = self.find_employee_by_name(name)
        # if there
        if emp:
            # assigning new updated salary to employees salary
            emp.salary = new_salary
            # returning True
            return True
        # if there is no any employee present by that name
        return False



