import cv2
import numpy as np
from djitellopy import Tello
from ultralytics import YOLO

model = YOLO("yolov8m_custom.pt")

tello = Tello()
tello.connect()
print(f"Battery: {tello.get_battery()}%")

tello.streamon()

while True:
    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (640, 480))

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = model.names[cls]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Tello YOLO Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


tello.streamoff()
cv2.destroyAllWindows()
