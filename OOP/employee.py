class Employee:
    xmas_perc_bonus = 0.30

    def __init__(self, emp_name, emp_number, _salary):
        self.emp_name = emp_name
        self.emp_number = emp_number
        self._salary = _salary

    def __repr__(self): #? This is the representation of the class
        return f"{self.emp_name}, {self.emp_number}, {self._salary}"

    @classmethod
    def from_str(cls, str_data):
        """A custom constructor for that parses str arguments

        Arguments:
            str_data {string} -- employee data separated by '-'

        Returns:
            Employee instance
        """
        emp_name, emp_number, _salary = str_data.split("-")
        return cls(emp_name, emp_number, int(_salary))

    def get_bonus(self):
        xmas_bonus = Employee.xmas_perc_bonus * self._salary
        return xmas_bonus

    def get_emp_info(self):
        emp_info = {
            "Employee Name" : self.emp_name,
            "Employee Number" : self.emp_number,
            "Salary" : self._salary
        }
        return emp_info

emp1 = Employee("Jeg Ramos", "201312416", 45500)
print(emp1.get_emp_info())
print(emp1.get_bonus())

emp2 = Employee("Sarah", "201312417", 80000)
print(emp2.get_emp_info())
print(emp2.get_bonus())

#? Passing a str to the contructor without parsing
emp3 = Employee.from_str("Jonathan Padios-201312418-90000")
print(emp3.get_emp_info())
print(emp3.get_bonus())

print(emp1)