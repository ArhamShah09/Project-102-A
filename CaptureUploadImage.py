import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame =  videoCaptureObject.read()
        image_name = "img"+str(number)+".jpg"
        cv2.imwrite(image_name, frame)
        start_time = time .time()
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return image_name

def upload_file(image_name):
    access_token = 'ScCnNIeInuUAAAAAAAAAAShZGoNpDyRkSfkOGJx7UaG_SeLI4Uq4KmPoVCqoRrJQ'
    file_name = image_name
    file_from = file_name
    file_to = "/UserPictures/"+(image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded.")

def main():
    while(True):
        if((time.time()-start_time) >= 10):
            name = take_snapshot()
            upload_file(name)

main()