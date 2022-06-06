from subscribers import PlanesOnGround
from subscribers import  PlanesInFlight
from subscribers import Runway

class Plane:
    def __init__(self, id: int):
        self.is_in_the_air = False
        self.id = id
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify(self):
        for sub in self.subscribers:
            sub.notify(self)

    def take_off(self):
        if (not self.is_in_the_air):
            print(f"Plane {self.id} is taking off...")
            self.is_in_the_air = True
            self.notify()

    def get_is_in_the_air(self):
        return self.is_in_the_air

    def set_is_in_the_air(self, is_in_the_air):
        self.is_in_the_air = is_in_the_air

    def get_id(self):
        return self.id


