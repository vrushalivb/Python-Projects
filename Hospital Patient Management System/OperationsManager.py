from Patient import *
from Specialization import *


class OperationsManager:
  def __init__(self):
    # creating 20 specializations each with its own queue with 10 capacity limit
    self.specializations = {i: Specialization(f"Spec {i}") for i in range(1,21)}

  def run(self):
    while True:
      print("\n--- Hospital System Menu ---")
      print("1) Add new patient")
      print("2) Print all patients")
      print("3) Get next patient")
      print("4) Remove a patient")
      print("5) End program")

      choice = input("Enter your choice (1-5): ")

      # Add new patient
      if choice == "1":
        spec = int(input("Enter specialization number between (1-20): "))
        name = input("Enter patient name: ")
        status = int(input("Enter status (0: Normal | 1: Urgent | 2: Super-Urgent): "))
        # checking if entered spec is in speacializations or not
        if spec in self.specializations:
          # if yes then adding that patient to that specific specialization
          self.specializations[spec].add_patients(name, status)
          print(f"\n patient {name} has added to specialization {spec}")
        else:
          print("Invalid specialization ID. Please try 1-20.")

          # Print all patients
      if choice == "2":
        found_patients = False
        # iterating one by one specialization and its id
        for i, spec in self.specializations.items():
            # also checking if patients are waiting in queue
          if spec.queue:
            found_patients = True
            print(f"\n specialization: {i}: ")
            # checking list of patients in specific specialization
            for p in spec.queue:
              # prints name and status (calls __str__() fucntion automaticall)
              print(p)
        if not found_patients:
          print(f"\n No patients in specialization")

      # Get next patient
      if choice == "3":
        spec = int(input("Enter specialization number between (1-20): "))
        # calls get() where it removes fisrt patient in queue and returns that patient object
        patient = self.specializations[spec].get_next_patient()
        # printing next patient if next patient is in queue otherwise it will go to else
        print(f"\nNext Patient: {patient}" if patient else "\nNo patients in queue")

      # Remove a patient
      if choice == "4":
        spec = int(input("Enter specialization number between (1-20): "))
        name = input("Enter patient name: ")
        #
        removed = self.specializations[spec].remove_by_name(name)
        print("\n Patient removed." if removed else "Patient not found.")

      # End program
      if choice == "5":
        print("Exiting the program.")
        break