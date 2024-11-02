# Circle Detection in Video Frames

This project uses OpenCV to detect and draw circles on frames of a video. The program processes each frame to grayscale, detects circles using the Hough Circle Transform, and then overlays detected circles on the original frame. The processed frames are displayed in real time. This script is modular, with specific functions for circle detection, drawing, image processing, and video frame display.

## Features

- **Circle Detection**: Detects circles in grayscale video frames using the Hough Circle Transform.
- **Real-Time Processing**: Processes and displays each frame in real-time as circles are detected.
- **Modular Code Structure**: Functions are organized by functionality for ease of maintenance and scalability.

## Project Structure

- **`main.py`**: Main script to read video frames, process them, and display results.
- **`circles.py`**: Contains functions to detect circles (`detect_circles`) and draw them on an image (`draw_circle`).
- **`display_image.py`**: Contains functions for image processing (`process_image`) and frame display (`display_video_frame`).

## How It Works

1. **Open Video File**: The program reads a specified video file frame by frame.
2. **Process Each Frame**: Each frame is converted to grayscale and blurred to reduce noise.
3. **Detect Circles**: Circles are detected using the Hough Circle Transform in the grayscale image.
4. **Draw Circles**: Detected circles are drawn on the original frame.
5. **Display Results**: The processed frame with circles is displayed in a window.

## Usage

1. **Prepare the Video File**:
   - Place the video file in the same directory as the script or provide a full path to the file.
   - Update the `capture = cv.VideoCapture("IMG_0257.mov")` line with the desired video file path if necessary.

2. **Run the Program**:
   - Run the main script:
     ```bash
     python main.py
     ```

3. **View Output**:
   - A window named "Video with Circles" will open, displaying each frame of the video with detected circles overlaid.

4. **Exit**:
   - The program will process all frames in the video. Close the window or press `ESC` to stop at any time.

## Functions

### Main Script (`main.py`)

- **Video Capture**: Opens and reads each frame of the video.
- **Processing Loop**: Processes each frame in real-time, detecting and drawing circles.
- **Display and Cleanup**: Displays the processed frames and releases resources upon completion.

### Circle Detection (`circles.py`)

- **`detect_circles(processed_img)`**: Detects circles in a grayscale image using Hough Circle Transform.
  - Parameters:
    - `processed_img`: Grayscale image to process.
  - Returns:
    - `circles`: Array of detected circles, or `None` if no circles are detected.
  
- **`draw_circle(img, circles)`**: Draws detected circles on the image.
  - Parameters:
    - `img`: Original image.
    - `circles`: Array of detected circles.
  - Returns:
    - `img`: Image with circles drawn.

### Image Processing and Display (`display_image.py`)

- **`process_image(img)`**: Converts an image to grayscale and applies blurring.
  - Parameters:
    - `img`: Original image.
  - Returns:
    - `gray`: Processed grayscale image.
  
- **`display_video_frame(frame, windowName)`**: Displays a video frame in a window.
  - Parameters:
    - `frame`: Processed frame with circles.
    - `windowName`: Title of the display window.

## Requirements

- **Python 3.x**
- **OpenCV (`cv2`)**
  - Install OpenCV via pip:
    ```bash
    pip install opencv-python
    ```

## Example

If your video file is named `IMG_0257.mov`, the program will open it and process each frame to detect circles. Detected circles will be highlighted in each frame and displayed in a window titled "Video with Circles."

