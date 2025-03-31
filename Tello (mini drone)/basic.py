import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
print(f"Battery: {tello.get_battery()}%")

tello.streamon()

while True:

    frame = tello.get_frame_read().frame
    img = cv2.resize(frame, (640, 480))  # Resize for display

    cv2.imshow("Tello Video Feed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
cv2.destroyAllWindows()
tello.end()
