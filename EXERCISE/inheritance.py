class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def display(self):
        print("Name : " +self.name)
        print("Age : " +str(self.age))
        print("Gender : " +self.gender)


class employee(Person):
    def __init__(self, name, age, gender,salary,job):
        super().__init__(name, age, gender)
        self.salary=salary
        self.job=job
    
    def display(self):
        super().display()
        print("Job : "+self.job)
        print("Salary : "+str(self.salary))

class Student:
    def __init__(self,classNo,id):
        self.classNo=classNo
        self.id=id
    def display(self):
        print("ID : "+str(self.id))
        print("ClassNo : "+str(self.classNo))

class Resident(Person,Student):
    def __init__(self, name, age, gender,classNo,id):
        Person.__init__(self,name, age, gender)
        Student.__init__(self,classNo,id)
    def display(self):
        Person.display(self)
        Student.display(self)


r1=Resident("brijesh",18,'Male',244,1234)
r1.display()

            

