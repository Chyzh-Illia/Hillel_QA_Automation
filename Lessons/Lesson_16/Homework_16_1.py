class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)  # Явный вызов конструктора Employee
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)  # Явный вызов конструктора Employee
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)  # Явный вызов конструктора Manager
        Developer.__init__(self, name, salary, programming_language)  # Явный вызов конструктора Developer
        self.team_size = team_size


def test_teamlead():
    team_lead = TeamLead("Alex", 100000, "IT", "Python", 5)
    assert hasattr(team_lead, "name"), "Attribute 'name' does not exist"
    assert hasattr(team_lead, "salary"), "Attribute 'salary' does not exist"
    assert hasattr(team_lead, "department"), "Attribute 'department' does not exist"
    assert hasattr(team_lead, "programming_language"), "Attribute 'programming_language' does not exist"
    assert hasattr(team_lead, "team_size"), "Attribute 'team_size' does not exist"
    print("Test passed, complete!")


test_teamlead()