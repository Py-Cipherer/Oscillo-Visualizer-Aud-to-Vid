import numpy as np
import cv2

W, H = 1080, 1920

def generate_frame(energy):
    frame = np.zeros((H, W, 3), dtype=np.uint8)

    radius = int(80 + energy * 500)
    glow = frame.copy()

    cv2.circle(glow, (W//2, H//2), radius, (120, 80, 255), -1)
    glow = cv2.GaussianBlur(glow, (0, 0), sigmaX=30)

    frame = cv2.addWeighted(glow, 0.6, frame, 0.4, 0)
    return frame
