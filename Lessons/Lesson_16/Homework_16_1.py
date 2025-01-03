class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Используем super() для MRO
        super(TeamLead, self).__init__(name, salary, department)
        self.programming_language = programming_language
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