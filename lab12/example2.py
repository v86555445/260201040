class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def set_name(self,name):
    self.name=name
  def get_name(self):
    return self.name