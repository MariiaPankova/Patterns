from abc import ABC,abstractmethod

class Command(ABC):
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def execute(self):
        pass


class OnCommand(Command):
    def execute(self):
        self.app.light_on()


class OffCommand(Command):
    def execute(self):
        self.app.light_off()




class Controller:
    def __init__(self, on_command, off_command):
        self.on_command = on_command
        self.off_command = off_command

    def on(self):
        self.on_command.execute()

    def off(self):
        self.off_command.execute()
