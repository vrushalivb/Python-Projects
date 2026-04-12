from Patient import *

class Specialization:

  # initilizing specializaton name, queue and max capacity
  def __init__(self, spec_name):
    # dept names
    self.spec_name = spec_name
    # initializing empty list to store patient objects
    self.queue = []
    # setting max capcity
    self.limit = 10

  # • Adding patients with various urgency levels.
  def add_patients(self, name, status):
    # checking if no of patients in list reached max capacity
    if len(self.queue) >= self.limit:
      print("Queue is full")
      return False

    # if queue is not full add
    # creating object of Patient class
    new_patient = Patient(name, status)

    # sorting patients status wise
    if status == 0:
      self.queue.append(new_patient)

    elif status == 1:
      # Insert after existing urgent/super-urgent but before normal
      idx = next((i for i, p in enumerate(self.queue) if p.status == 0), len(self.queue))
      self.queue.insert(idx, new_patient)

    elif status == 2:
            # Insert after existing super-urgent but before urgent/normal
            idx = next((i for i, p in enumerate(self.queue) if p.status < 2), len(self.queue))
            self.queue.insert(idx, new_patient)
    return True


  # • Retrieving the next patient from the queue
  def get_next_patient(self):
    # checking if there are an patient in queue if yes then delete first patient in queue and if queue is empty then send None
    return self.queue.pop(0) if self.queue else None

  #• Removing patients by name
  def remove_by_name(self,name):
    # checking one by one patient names and its index
    for i, patient in enumerate(self.queue):
      if patient.name.lower() == name.lower():
        # deleting index wise
        return self.queue.pop(i)
    return None

  # • Checking queue capacity
  def check_patient_capacity(self):
    return len(self.queue)

