import numpy as np
import cv2


# Help taken from https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html

# Function for reading the camera input
def read_webcam_input():
    vc = cv2.VideoCapture(0)

    # Camera is not accessible
    if not vc.isOpened():
        print("Camera not accessible")

    while True:
        ret, frame = vc.read()  # Reading frames
        if not ret:
            print("Unable to read frames")

        # Flipping the camera to get mirroring effect
        frame = cv2.flip(frame, 1)
        a, b, c = np.shape(frame)  # Shape of the frame

        # Text Input (My Name)
        name = "Shashwat Pathak"
        # Getting the pixel size of the text in the image
        size = cv2.getTextSize(name, fontFace=cv2.FONT_ITALIC, fontScale=1, thickness=1)
        # Using the pixel size of the text, and shape of the frame to place it on the window
        image = cv2.putText(frame, "Shashwat Pathak", org=(b-size[0][0]-2, size[0][1]+2), fontFace=cv2.FONT_ITALIC,
                            fontScale=1, color=(0, 0, 255), thickness=1)
        # Adding the rectangular boundary to the name with an offset of 4 dpi
        rect_image = cv2.rectangle(image, pt1=(b-size[0][0]-4, size[0][1]+4), pt2=(b-1, 1), color=(0, 255, 0))

        # Computing the same for grayscale images
        gray_scale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_scale_with_name = cv2.putText(gray_scale_image, "Shashwat Pathak", org=(b-size[0][0]-2, size[0][1]+2),
                                           fontFace=cv2.FONT_ITALIC, fontScale=1, color=255, thickness=1)
        gray_scale_with_rect = cv2.rectangle(gray_scale_with_name, pt1=(b-size[0][0]-4, size[0][1]+4), pt2=(b-1, 1), color=255)

        cv2.imshow('frame1', rect_image)
        cv2.imshow('frame2', gray_scale_with_rect)
        cv2.moveWindow('frame1', 350, 200)
        x, y, w, h = cv2.getWindowImageRect('frame1')
        cv2.moveWindow('frame2', x+w, 200)
        if cv2.waitKey(1) == ord('q'):
            break

    vc.release()
    cv2.destroyAllWindows()

    return


if __name__ == '__main__':
    read_webcam_input()