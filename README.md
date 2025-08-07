 **Real-Time Object Detection with Flask and YOLOv3**  

📌 **A simple Flask web app that streams real-time video from a webcam and performs object detection using YOLOv5.**  

## 📸 **About**  
The application captures frames from a webcam, processes them with an object detection model, and streams the results to a web browser.  

---

## 🚀 **Features**  

- 🔹 **Real-time object detection** using **YOLOv3**  
- 🔹 **Flask-based web application** for easy streaming  
- 🔹 **Live video feed with detected objects**  
- 🔹 **Runs on any system with OpenCV, PyTorch, and Flask installed**  

---

## 🛠 **Installation and Setup**  

### **1
 Clone the Repository**  
```bash
git clone[ https://github.com/your-username/your-repository.git](https://github.com/Noba21/real-time-object-detection.git)
cd your-repository
```

### **2 Install Dependencies**  
Make sure you have Python installed (recommended: Python 3.8+). Then, install the required packages:  

```bash
pip install flask opencv-python torch torchvision
```
### **3 Download yolo**  
download the yolov3 "weight and cfg" file from the internt

### **4 Run the Application**  
```bash
python app.py
```

### **5 Open the Web App**  
Once the server is running, open your browser and go to:  
```
http://127.0.0.1:5000/
```

---

## 🔧 **How It Works**  

1️⃣ Captures video frames from the webcam using **OpenCV**.  
2️⃣ Runs object detection using **YOLOv3**.  
3️⃣ Processes and draws bounding boxes on detected objects.  
4️⃣ Streams the processed frames to a web browser in real time using **Flask**.  

---

## 📁 **Project Structure**  

```
📂 your-repository
│── app.py            # Main Flask app with real-time object detection
│── templates/
│   ├── index.html    # HTML page to display the video stream
│── static/           # Static files (CSS, JS, etc.)
│── README.md         # Documentation
```

---

## 🤖 **Future Improvements**  

✅ Support for **custom YOLO models**  
✅ Add **recording functionality**  
✅ Deploy on a cloud server  



---

💡 **Made with ❤️ using Flask, OpenCV, and YOLOv3!**  

---

