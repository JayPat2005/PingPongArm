# 🏓 Robotic Ping Pong Arm

## 🔗 Project Link
GitHub Repository: https://github.com/JayPat2005/PingPongArm

---

## 📌 Project Overview
This project is a robotic system designed to track and hit a ping pong ball in real time. It combines **computer vision, physics-based trajectory prediction, and robotics control** to create an automated ping pong playing arm.

The system detects the ball, predicts its path, and moves a robotic arm to intercept and return the ball accurately.

---

## ⚙️ What It Does
- Tracks a ping pong ball using camera-based computer vision  
- Predicts the ball’s trajectory using physics modeling  
- Calculates arm movement using inverse kinematics  
- Moves a robotic arm to hit the ball in real time  

---

## 🛠️ How It Was Built

### 1. Computer Vision (Python)
- Used masking and filtering to isolate the ping pong ball  
- Extracted position coordinates frame-by-frame  
- Implemented Single Object Tracking (SOT)  

### 2. Trajectory Prediction
- Applied motion physics to estimate ball path  
- Predicted future position before impact  

### 3. Robotics System
- Built a 3-foot robotic arm  
- Controlled using a Raspberry Pi  
- Integrated stepper motors and drivers  

### 4. Inverse Kinematics
- Calculated joint angles required to reach target position  
- Enabled precise positioning for ball contact  

---

## 💻 Tools & Technologies
- Python  
- Raspberry Pi  
- Stepper Motors + Motor Drivers  
- Matplotlib  
- Computer Vision (OpenCV concepts)  
- Custom Mechanical Design  

---

## 🔄 Development Process
1. Built initial ball detection system  
2. Implemented trajectory prediction model  
3. Designed and assembled robotic arm  
4. Integrated hardware and software  
5. Tested and optimized accuracy  

---

## 🧠 Challenges & Fixes
- **Detection noise** → Improved masking and filtering  
- **Prediction inaccuracies** → Refined physics calculations  
- **Motor precision issues** → Calibrated stepper motors  
- **Timing delays** → Optimized real-time response  

---

## 🎥 Demo Video
[Watch Demo Here](**https://youtu.be/_fZSaP1G6ps**)

*(Include a short screen recording demonstrating tracking + arm movement with audio explanation.)*

---

## 🚀 Summary
This project demonstrates the integration of:
- Computer Vision  
- Real-Time Systems  
- Robotics  
- Embedded Systems  

It highlights the ability to combine software and hardware to solve a real-world problem involving motion tracking and automation.
