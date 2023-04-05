import cv2

# Define the index numbers of your cameras
camera_1_index = 0
camera_2_index = 1

# Create VideoCapture objects for each camera
cap1 = cv2.VideoCapture(camera_1_index) # très interessant de voir qu'il ouvre les 2 flux !
cap2 = cv2.VideoCapture(camera_2_index) # très interessant de voir qu'il ouvre les 2 flux !

if not (cap1.isOpened() and cap2.isOpened()):
    print("Error: Unable to open one or more cameras.")
    exit()

current_camera = cap1

try:
    while True:
        # Capture frame-by-frame
        ret, frame = current_camera.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF

        # Press 'q' to exit the loop
        if key == ord('q'):
            break

        # Press 's' to switch cameras
        if key == ord('s'):
            if current_camera == cap1:
                current_camera = cap2
            else:
                current_camera = cap1
finally:
    # Release the VideoCapture objects and close the window
    cap1.release()  # Important de savoir si ce n'est pas bien fait dans le code de Xojo qui ne switch pas bien entre les caméras
    cap2.release()
    cv2.destroyAllWindows()
