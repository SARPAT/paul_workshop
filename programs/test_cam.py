import cv2

# Test camera indices
for i in range(3):  # Try indices 0, 1, 2
    cam = cv2.VideoCapture(i)
    if cam.isOpened():
        ret, frame = cam.read()
        if ret:
            print(f"Camera found at index {i}")
            print(f"Frame shape: {frame.shape}")
        cam.release()
    else:
        print(f"No camera at index {i}")