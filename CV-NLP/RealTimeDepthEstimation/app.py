from flask import Flask, Response, stream_with_context
import cv2
from depth_estimation import estimate_depth

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    """Stream video from the camera and return depth maps in real-time."""
    video_capture = cv2.VideoCapture(0)  # Capture video from the first camera device

    def generate_frames():
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            depth_map = estimate_depth(frame)  # Convert the frame to a depth map
            ret, buffer = cv2.imencode('.jpg', depth_map)  # Encode the depth map as a JPEG
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Stream the depth map

    return Response(stream_with_context(generate_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
