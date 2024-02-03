import cv2 as cv #import open cv library for image processing functionality
# Importing functions for circle detection and drawing from the 'circles' module
from circles import detect_circles, draw_circle
# Importing functions for image processing and video frame display from the 'display_image' module
from display_image import process_image, display_video_frame

if __name__ == "__main__":
    # Open the video file for capturing frames
    capture = cv.VideoCapture("IMG_0257.mov")

    # Loop to process and display each frame of the video
    while True:
        # Read the next frame from the video
        frame_exist, img = capture.read()

        # Check if the frame was successfully read
        if frame_exist:
            # Process the frame to grayscale
            gray_img = process_image(img)

            # Detect circles in the processed grayscale frame
            circles = detect_circles(gray_img)

            # Draw circles on the original frame
            img_with_circles = draw_circle(img.copy(), circles)

            # Display the original frame with circles
            display_video_frame(img_with_circles, "Video with Circles")
        else:
            # Break the loop if no more frames are available
            break

    # Release the video capture object
    capture.release()
    # Close all OpenCV windows
    cv.destroyAllWindows()
