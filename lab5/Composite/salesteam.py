from expenses_payer import ExpensesPayer

class Salesteam(ExpensesPayer):
    def __init__(self, team: list):
        self.team = team

    def get_team(self):
        return self.team

    def remove_person(self, person):
        if person in self.team:
            self.team.remove(person)

    def add_person(self, person):
        self.team.append(person)

    def pay_expenses(self, amount):
        for person in self.team:
            person.pay_expenses(amount)
