from lamp import *
from controller import *


if __name__ == '__main__':
    kitchen = Lamp("Kitchen")
    hall = Lamp("Hall")
    bedroom = Lamp("Bedroom")
    bathroom = Lamp("Bathroom")
    home_lights = HomeLights([kitchen, hall, bathroom, bedroom])

    kitchen_controller = Controller(OnCommand(kitchen), OffCommand(kitchen))
    hall_controller = Controller(OnCommand(hall), OffCommand(hall))
    bedroom_controller = Controller(OnCommand(bedroom), OffCommand(bedroom))
    bathroom_controller = Controller(OnCommand(bathroom), OffCommand(bathroom))
    universal_controller = Controller(OnCommand(home_lights), OffCommand(home_lights))

    kitchen_controller.on()
    hall_controller.on()
    bedroom_controller.on()
    bathroom_controller.on()

    hall_controller.off()
    kitchen_controller.off()

    print('===============')
    universal_controller.off()
    bathroom_controller.on()

    print('===============')
    universal_controller.on()



