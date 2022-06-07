from lamp import Lamp
from controller import *


if __name__ == '__main__':
    lamp = Lamp("Night lights")
    controller = Controller(OnCommand(lamp), OffCommand(lamp))

    controller.on()
    controller.off()
    controller.off()
    controller.on()