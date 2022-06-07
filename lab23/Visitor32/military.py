from visitor import *


class GeneralStaff():
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."

    def accept(self, visitor):
        visitor.visit_staff(self)


class MilitaryBase():
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

    def accept(self, visitor):
        visitor.visit_base(self)


if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

    spy = SecretAgent()
    saboteur = Saboteur()
    generalStaff.accept(spy)
    militaryBase.accept(spy)
    generalStaff.accept(saboteur)
    militaryBase.accept(saboteur)
