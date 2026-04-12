class Employee:
  # initializing name, age and salary
  # will run when we create object and saves these details into object
  def __init__(self,name,age,salary):
    # instance object - stores specific data for each employee(each object)
    self.name = name
    self.age = age
    self.salary = salary

  # special python method - which tells python eaxctly how to print employee object
  def __str__(self):
    return f"Name : {self.name} | Age : {self.age} | Salary : {self.salary}"