from device import *
from controller import  *

if __name__ == '__main__':
    tv = Television()
    print(1)
    remote = Controller(OnCommand(tv),
                        OffCommand(tv),
                        VolumeUpCommand(tv),
                        VolumeDownCommand(tv),
                        NextChanelCommand(tv),
                        PrevChanelCommand(tv))

    radio = Radio(chanel=2)
    radio1 = Radio(volume=0)

    multi_remote = Multicontroller([tv, radio, radio1],
                        OnCommand,
                        OffCommand,
                        VolumeUpCommand,
                        VolumeDownCommand,
                        NextChanelCommand,
                        PrevChanelCommand)
    multi_remote.device_on()

    for i in range(30):
        remote.device_next_chanel()
    multi_remote.device_volume_up()
    remote.device_volume_down()
    multi_remote.device_volume_down()

    remote.device_prev_chanel()

    multi_remote.device_off()