class Employee:   'Common base class for all employees'   # class variable that counts number of employees   __empCount = 0   def __init__(self, name, salary):      # object attributes      self.name = name      self.salary = salary      # increase the employee count      Employee.__empCount += 1      # method that displays the total number of employees   def displayCount(self):     print "Total Employee %d" % Employee.__empCount            # displays information about an Employee   def displayEmployee(self):      print "Name : ", self.name,  ", Salary: ", self.salaryclass Developer(Employee):      def __init__(self, name, salary, position='middle'):      Employee.__init__(self, name, salary)      self.position = position   def displayEmployee(self):      print "Name : ", self.name,  ", Salary: ", self.salary, ", position: ", self.positionprint dir(Employee)print Employee._Employee__empCounte1 = Employee("Ivan", 1500)d1 = Developer("Vasiliy", 2000)d1.displayEmployee()d1.
