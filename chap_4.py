class car : 
    brand = "toyota"
    name= "Bisma"
    
    def __init__(self,name): # Self : storing the current instance of class 
            self.name = name


    def get_cgpa(self):
          return self.get_cgpa
    

car1 = car(" Raza")
car2 = car(" Shrada")
print(car1.name)
print(car2.name)

car1.get_cgpa()
car2.get_cgpa()
