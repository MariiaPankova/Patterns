from fan import Fan
from states import *

if __name__ == '__main__':
    fan = Fan()
    fan.set_state(LowState(fan))
    fan.turn_up()
    fan.turn_up()
    fan.turn_down()
    fan.turn_down()
    fan.turn_up()