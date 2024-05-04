import machine
import camera
import urequests
import time

led = machine.Pin(4, machine.Pin.OUT)
led.on()
time.sleep(0.2)
led.off()

def setupcamera():
  camera.init()  
def takephoto(buf):
  led.on()
  time.sleep(0.2)
  buf=camera.camera.capture_jpg()
  led.off()
def sendtg(token,chatid,buf)
  setupcamera()
  takephoto(buf)
  
