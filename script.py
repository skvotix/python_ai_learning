class DataDescriptor:
    def __init__(self, expected_type):
        self.expected_type = expected_type


    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}, got {type(value)}")

        setattr(instance, self.name, value)



class NonDataDescriptor:
    def __init__(self, default_value):
        self.default_value = default_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return self.default_value

class User:
    name = DataDescriptor(str)
    age = DataDescriptor(int)
    role = NonDataDescriptor("user")
    theme = NonDataDescriptor("light")

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def give_a_role(self, role):
        self.role = role

    def switch_theme(self):
        if self.theme == "light":
            self.theme = "dark"
        elif self.theme == "dark":
            self.theme = "light"
        else:
            self.theme = "light"


    def __str__(self):
        return f"{self.name} {self.age} {self.role} {self.theme}"


user = User("Illia", 17)
print(user)
user.give_a_role("king")
print(user.role)
user.switch_theme()
print(user)