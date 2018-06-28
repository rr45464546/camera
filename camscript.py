from picamera import PiCamera
from time import sleep
from PIL import Image

camera = PiCamera()
camera.start_preview();sleep(5);camera.capture('/home/pi/tempimg.png');camera.stop_preview()

im = Image.open('/home/pi/tempimg.png').crop((315,0,1365,1050))
im2 = Image.open('/home/pi/tempimg.png').crop((315,0,1365,1050))
imoverlay = Image.open('/home/pi/overlay.png')

newdata = []

for a,b in zip(im.getdata(),imoverlay.getdata()):
    if b[3]==0:
        newdata.append(a)
    else:
        newdata.append(b)

im2.putdata(newdata)
im2.save('/home/pi/Desktop/final.png')
