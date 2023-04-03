import cv2

def main():
    # Open the default camera (0) or use the camera index if you have multiple webcams.
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame is not read correctly, break the loop
        if not ret:
            break

        # Display the resulting frame
        cv2.imshow('Webcam Test', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()