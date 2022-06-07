from abc import ABC,abstractmethod

class Device(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def next_chanel(self):
        pass

    @abstractmethod
    def prev_chanel(self):
        pass


class Television(Device):
    def __init__(self, is_On=False, volume=50, chanel=1):
        self.is_on = is_On
        self.volume = volume
        self.chanel = chanel

    def on(self):
        if self.is_on:
            return
        print("TV is on")
        self.is_on = True

    def off(self):
        if not self.is_on:
            return
        print("TV is off")
        self.is_on = False

    def volume_up(self):
        if self.is_on:
            self.volume += 1
            print('Volume =', self.volume)

    def volume_down(self):
        if self.is_on:
            self.volume -= 1 if self.volume > 0 else 0
            print('Volume =', self.volume)

    def next_chanel(self):
        if self.is_on:
            self.chanel += 1
            print(f'Channel = {self.chanel}')

    def prev_chanel(self):
        if self.is_on:
            self.chanel -= 1 if self.chanel > 0 else 0
            print(f'Channel = {self.chanel}')


class Radio(Device):
    def __init__(self, is_On=False, volume=50, chanel=1):
        self.is_on = is_On
        self.volume = volume
        self.chanel = chanel

    def on(self):
        if self.is_on:
            return
        print("Radio is on")
        self.is_on = True

    def off(self):
        if not self.is_on:
            return
        print("Radio is off")
        self.is_on = False

    def volume_up(self):
        if self.is_on:
            self.volume += 1
            print('Radio Volume =', self.volume)

    def volume_down(self):
        if self.is_on:
            self.volume -= 1 if self.volume > 0 else 0
            print('Radio Volume =', self.volume)

    def next_chanel(self):
        if self.is_on:
            self.chanel += 1
            print(f'Radio Channel = {self.chanel}')

    def prev_chanel(self):
        if self.is_on:
            self.chanel -= 1 if self.chanel > 0 else 0
            print(f'Radio Channel = {self.chanel}')