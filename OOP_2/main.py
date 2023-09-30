class Student():
    all = []
    def __init__(self, name, username, year_old):
        assert year_old >= 0, f"This year_old {year_old} very small"
        
        self.name = name
        self.username  = username
        self.year_old = year_old
        
        Student.all.append(self)
        
        def About(self):
           return(f"Ismim {self.name} {self.username} {self.year_old} yoshdaman")
student1 = Student('Murodulla', "Ismoilov", 2007)
print(student1)
print(Student.all)

