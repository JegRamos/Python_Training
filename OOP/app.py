# Classes should be named in upper camel case
class User:
    def __init__(self, name, _password):
        self.name = name
        self._password = _password
    pass

user1 = User("John", "65544411")
print(user1.name)
print(user1._password)
