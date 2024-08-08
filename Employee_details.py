class Employee:
    def __init__(self):
        self.name=" "
        self.empld=" "
        self.dept=" "
        self.salary=" "
    def getEmpDetails(self):
        self.name=input("Enter Employee name:")
        self.empld=input("Enter Employee ID:")
        self.dept=input("Enter Employee department:")
        self.salary=input("Enter Employee salary:")
    def showEmpDetails(self):
        print("Employee Detais")
        print("Name:",self.name)
        print("ID:",self.empld)
        print("Dept:",self.dept)
        print("Salary:",self.salary)
    def updtSalary(self):
        self.salary=int(input("Enter new salary"))
        print("Updated Salary",self.salary)
e1=Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()