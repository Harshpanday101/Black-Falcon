# **FOD Detection Drone System**

## **Project Overview**
The **Foreign Object Debris (FOD) Detection Drone System** is an autonomous drone-based solution designed to enhance runway safety by detecting and identifying debris on airport runways. The system uses **machine learning (ML) algorithms** for object detection and classification, achieving 92% accuracy in identifying small objects like nuts and bolts. It consists of:
- **DJI Tello Drone** for preliminary testing and simulations.
- **Machine Learning Model** for FOD detection.
- **Raspberry Pi-based Autonomous Drone** for real-world deployment.

## **Features**
- **Real-time FOD detection** using computer vision and deep learning.
- **Swarm coordination** for large-scale runway monitoring.
- **Return-to-Launch (RTL) functionality** for autonomous operations.
- **WiFi-based data transmission** for real-time alerts.
- **Falcon Scann application** for live monitoring and user interaction.

## **Project Structure**
```
├── dji_tello_drone/      # Code and scripts for DJI Tello Drone
│   ├── tello_control.py  # Controls DJI Tello for testing
│   ├── tello_stream.py   # Video streaming from Tello
│   
│
├── ml_model/             # Machine learning model for FOD detection
│   ├── train.py          # Training script for ML model
│   ├── detect.py         # Inference script for detecting FOD
│   ├── model.pth         # Trained ML model
│   
│
├── raspi_autonomous_drone/  # Code for Raspberry Pi-based autonomous drone
│   ├── flight_control.py    # Drone flight control script
│   ├── object_detection.py  # Runs ML model on real-time drone feed
│   ├── telemetry.py         # Collects and sends telemetry data
│  
│
└── README.md             # Main project documentation
```

## **Installation and Setup**
### **1. Setting Up DJI Tello Drone**
1. Install dependencies:
   ```bash
   pip install djitellopy opencv-python
   ```
2. Run the control script:
   ```bash
   python dji_tello_drone/tello_control.py
   ```

### **2. Running the Machine Learning Model**
1. Install dependencies:
   ```bash
   pip install torch torchvision opencv-python numpy
   ```
2. Run the detection script:
   ```bash
   python ml_model/detect.py --image sample_image.jpg
   ```

### **3. Setting Up Raspberry Pi Autonomous Drone**
1. Install necessary libraries on Raspberry Pi:
   ```bash
   sudo apt-get install python3-opencv
   pip install numpy dronekit
   ```
2. Run the autonomous flight and object detection:
   ```bash
   python raspi_autonomous_drone/flight_control.py
   ```

## **Contributors**
- **Harsh Panday**
- **Anjali Aggarwal**
- - **Akash Lakhwan**



## **Future Improvements**
- **Integration of LiDAR and thermal imaging** for night-time operations.
- **Cloud-based analytics and predictive maintenance**.
- **Enhanced swarm coordination algorithms** for improved runway coverage.



