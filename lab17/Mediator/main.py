from plane import Plane
from subscribers import *

if __name__ == '__main__':
    plane = Plane(123)
    planes_up = PlanesInFlight()
    planes_down = PlanesOnGround()
    runway = Runway()
    plane.subscribe(planes_up)
    plane.subscribe(planes_down)
    plane.subscribe(runway)

    plane.take_off()