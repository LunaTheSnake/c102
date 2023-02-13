import cv2
import random
import time
start_time=time.time()
def take_snapshot():
    number=random.randint(0,10)
    video_capture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video_capture.read()
        image_name="picture"+str(number)+".jpg"

        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("snapshot_tacking")
    video_capture.release()
    cv2.destroyAllWindows()
def main():
    while(True):
        if((time.time()-start_time)>=5):
            take_snapshot()

main()