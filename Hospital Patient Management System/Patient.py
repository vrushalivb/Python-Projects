# from OperationsManager import *
# from Specialization import *

class Patient:
  # Initializing name and status
  def __init__(self, name, status):
    self.name = name
    # which can be 0 (normal), 1 (urgent), or 2 (super-urgent).
    self.status = status

  def __str__(self):
    # creating dictionary for status
    status_str = {0: "Normal", 1: "Urgent", 2: "Super-Urgent"}
    # printing details
    # checks number stored in self.status(if 1 then takes "urgent")
    # return f"Patient: {self.name} | status : {status_str.get(self.status)}"
    return f"Patient: {self.name:<15} | Status: {status_str[self.status]}"