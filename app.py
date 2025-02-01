from flask import Flask, render_template, Response
import cv2
import torch

# Initialize Flask app
app = Flask(__name__)

# Load object detection model (YOLOv5 example, replace with your own model if needed)
model = torch.hub.load('yolov3.cfg', 'yolov3.weights')

# Initialize webcam (index 0 is usually the default webcam)
camera = cv2.VideoCapture(0)


def generate_frames():
    """
    Capture video frames from the webcam, run object detection, and yield the results.
    """
    while True:
        success, frame = camera.read()  # Read a frame from the webcam
        if not success:
            break
        else:
            # Convert BGR (OpenCV default) to RGB for model input
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Run object detection on the frame
            results = model(rgb_frame)

            # Render the results (draw bounding boxes, labels, etc.)
            results.render()
            detection_frame = results.imgs[0]  # First processed frame

            # Convert RGB (from results) back to BGR for OpenCV compatibility
            detection_bgr_frame = cv2.cvtColor(detection_frame, cv2.COLOR_RGB2BGR)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', detection_bgr_frame)
            frame = buffer.tobytes()

            # Yield the frame as an HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """
    Route to stream video frames to the browser.
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
