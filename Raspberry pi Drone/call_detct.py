import cv2
import socket
import struct
import pickle
import torch
import pyttsx3
import threading
import queue
import time
from ultralytics import YOLO


engine = pyttsx3.init()
engine.setProperty('rate', 150)


model = YOLO(r"C:\Users\cnpan\Desktop\FOD\yolov8m_custom.pt")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.1.32.239', 9999))

data = b""
payload_size = struct.calcsize("Q")

speaking = False
last_spoken_time = 0
frame_queue = queue.Queue(maxsize=5)
result_queue = queue.Queue()


allowed_classes = {0, 1}


def detect_fod():
    """Thread function to process frames asynchronously."""
    global speaking, last_spoken_time

    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()

            # Perform detection
            results = model(frame)

            fod_detected = False
            for result in results:
                for box in result.boxes:
                    cls = int(box.cls[0].item())  # Get class ID

                    if cls in allowed_classes:  # Only detect nuts and bolts
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = box.conf[0].item()
                        label = f"{model.names[cls]}: {conf:.2f}"

                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                        fod_detected = True

            # Speak only once every 5 seconds
            current_time = time.time()
            if fod_detected and not speaking and (current_time - last_spoken_time > 5):
                speaking = True
                last_spoken_time = current_time
                threading.Thread(target=speak_alert).start()

            result_queue.put(frame)  # Store the processed frame


def speak_alert():
    """Thread function to announce FOD detection."""
    global speaking
    engine.say("Foreign Object Debris detected")
    engine.runAndWait()
    speaking = False  # Reset flag



threading.Thread(target=detect_fod, daemon=True).start()

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4096)
        if not packet:
            break
        data += packet


    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4096)

    # Deserialize frame
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)


    frame = cv2.resize(frame, (640, 480))


    if not frame_queue.full():
        frame_queue.put(frame)

    if not result_queue.empty():
        processed_frame = result_queue.get()
        cv2.imshow("YOLOv8 Detection", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
