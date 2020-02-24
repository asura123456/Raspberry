import time
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture('img5.jpg')
camera.stop_preview()

