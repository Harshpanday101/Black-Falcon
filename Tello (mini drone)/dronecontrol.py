from djitellopy import Tello
import time

tello = Tello()

tello.connect()
print(f"Battery: {tello.get_battery()}%")

tello.takeoff()
time.sleep(2)

print("Moving forward")
tello.move_forward(150)
time.sleep(2)

tello.move_left(150)
time.sleep(2)

print("Moving backward")
tello.move_back(150)
time.sleep(2)

tello.move_right(150)
time.sleep(2)

tello.land()
print("Landing")

tello.end()