import cv2
def take_snapshot():
    video_capture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video_capture.read()
        cv2.imwrite("picture.jpg",frame)
        result=False
    video_capture.release()
    cv2.destroyAllWindows()

take_snapshot()