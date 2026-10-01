class Employee:
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name= first_name
        self.last_name= last_name
        self.annual_salary= annual_salary
        self.raises= 5000
        
    def show_info(self):
        person=f"{self.first_name} {self.last_name}"
        print(person.title())

    def net_annual_salary(self):
        self.annual_salary+= self.raises
        print(f"Total net salary: ${self.annual_salary}")
        
    def give_custom_raise(self,c_raise):
        self.annual_salary+=c_raise
        print(f"Total net salary: ${self.annual_salary}")

    
