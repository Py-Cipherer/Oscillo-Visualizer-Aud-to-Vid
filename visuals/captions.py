import cv2

def draw_caption(frame, text):
    cv2.putText(frame,text.upper(),(80, 1550),
                cv2.FONT_HERSHEY_SIMPLEX,1.3,
                (220, 220, 220),2,cv2.LINE_AA)
    
    return frame
