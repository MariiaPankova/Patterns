from abc import ABC,abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def notify(self, plane):
        pass


class Runway(Subscriber):
    def __init__(self):
        self.is_awailable = True

    def set_is_awailable(self, is_awailable: bool):
        self.is_awailable = is_awailable

    def get_is_awailable(self):
        return self.is_awailable

    def notify(self, plane):
        self.set_is_awailable(False)
        print('Runway now unawailable')


class PlanesOnGround(Subscriber):
    def __init__(self):
        self.planes = [];

    def add_plane(self, plane):
        self.planes.append(plane)

    def remove_plane(self, plane):
        if plane in self.planes:
            self.planes.remove(plane)

    def notify(self, plane):
        if plane.get_is_in_the_air():
            self.remove_plane(plane)
        else:
            self.add_plane(plane)
        print(f'Plain on ground now: {plane in self.planes}')


class PlanesInFlight(Subscriber):
    def __init__(self):
        self.planes = [];

    def add_plane(self, plane):
        self.planes.append(plane)

    def remove_plane(self, plane):
        if plane in self.planes:
            self.planes.remove(plane)

    def notify(self, plane):
        if plane.get_is_in_the_air():
            self.add_plane(plane)
        else:
            self.remove_plane(plane)
        print(f'Plain in the air now: {plane in self.planes}')
