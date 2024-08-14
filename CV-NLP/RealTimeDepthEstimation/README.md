# Real-Time Depth Estimation with Flask

This project is a Flask application that captures video from a camera, processes each frame to generate depth maps using the MiDaS model, and streams the depth maps in real-time.

## Requirements

- Python 3.8 or higher
- Camera device (e.g., webcam)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/shafnashajahan/CV-NLP-Projects.git
    cd your-repo
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:

    - **Windows**:

        ```bash
        .venv\Scripts\activate
        ```

    - **macOS/Linux**:

        ```bash
        source .venv/bin/activate
        ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:

    ```bash
    python app.py
    ```

2. **Access the video feed**:

    Open your web browser and navigate to `http://localhost:5000/video_feed` to view the real-time depth map stream.

## Code Overview

- **app.py**: Contains the Flask application that streams the depth map from the camera.
- **depth_estimation.py**: Implements the depth estimation using the MiDaS model. Ensure this file contains the `estimate_depth` function.

## Troubleshooting

- **Camera Access Issues**: Ensure your camera is correctly connected and accessible. Check the camera index in `cv2.VideoCapture(0)`.
- **Dependency Errors**: Verify that all dependencies are installed correctly. Consider creating a new virtual environment and reinstalling the dependencies.

## Acknowledgments

- MiDaS model for depth estimation: [intel-isl/MiDaS](https://github.com/intel-isl/MiDaS)
- Flask for web framework
- OpenCV for image processing and video capture
