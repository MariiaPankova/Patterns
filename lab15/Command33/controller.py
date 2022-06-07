from abc import ABC,abstractmethod

class Command(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def execute(self):
        pass


class OnCommand(Command):
    def execute(self):
        self.device.on()


class OffCommand(Command):
    def execute(self):
        self.device.off()


class VolumeUpCommand(Command):
    def execute(self):
        self.device.volume_up()


class VolumeDownCommand(Command):
    def execute(self):
        self.device.volume_down()


class NextChanelCommand(Command):
    def execute(self):
        self.device.next_chanel()


class PrevChanelCommand(Command):
    def execute(self):
        self.device.prev_chanel()


class Controller:
    def __init__(self, on_comm, off_comm,
                        vol_up_comm, vol_down_comm,
                        next_ch_comm, prev_ch_comm):
        self.on_comm = on_comm
        self.off_comm = off_comm
        self.vol_up_comm = vol_up_comm
        self.vol_down_comm = vol_down_comm
        self.next_ch_comm = next_ch_comm
        self.prev_ch_comm = prev_ch_comm

    def device_on(self):
        self.on_comm.execute()

    def device_off(self):
        self.off_comm.execute()

    def device_volume_up(self):
        self.vol_up_comm.execute()

    def device_volume_down(self):
        self.vol_down_comm.execute()

    def device_next_chanel(self):
        self.next_ch_comm.execute()

    def device_prev_chanel(self):
        self.prev_ch_comm.execute()


class Multicontroller:
    def __init__(self, devices,
                        on_comm, off_comm,
                        vol_up_comm, vol_down_comm,
                        next_ch_comm, prev_ch_comm):
        self.devices = devices
        self.on_comm = on_comm
        self.off_comm = off_comm
        self.vol_up_comm = vol_up_comm
        self.vol_down_comm = vol_down_comm
        self.next_ch_comm = next_ch_comm
        self.prev_ch_comm = prev_ch_comm

    def device_on(self):
        for d in self.devices:
            self.on_comm(d).execute()

    def device_off(self):
        for d in self.devices:
            self.off_comm(d).execute()

    def device_volume_up(self):
        for d in self.devices:
            self.vol_up_comm(d).execute()

    def device_volume_down(self):
        for d in self.devices:
            self.vol_down_comm(d).execute()

    def device_next_chanel(self):
        for d in self.devices:
            self.next_ch_comm(d).execute()

    def device_prev_chanel(self):
        for d in self.devices:
            self.prev_ch_comm(d).execute()
