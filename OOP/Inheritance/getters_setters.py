class Employee:
    emp_count = 0

    def __init__(self, emp_name, _emp_title):
        self.emp_name = emp_name
        self._emp_title = _emp_title #! Private Attribute
        Employee.emp_count += 1

    def __repr__(self):
        return f"{self.emp_name} is a {self._emp_title}"

    @property
    def emp_title(self):
        return self._emp_title

    @emp_title.setter
    def emp_title(self, value_title):
        if value_title in ("Test Engineer", "Admin", "NTC", "Director"):
            self._emp_title = value_title
        else:
            raise ValueError("Invalid Job Title!")

jeg = Employee("Jeg Ramos", "Test Engineer")
print(jeg)
jeg.emp_title = "Admin"
print(jeg)
jeg.emp_title = "CEO"