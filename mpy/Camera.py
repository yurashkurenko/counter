import machine
led = machine.Pin(4, machine.Pin.OUT)
import camera
camera.init(0, format=camera.JPEG, fb_location=camera.DRAM)
import time
led.on()
time.sleep(1)
camera.init(0, format=camera.JPEG, fb_location=camera.DRAM)
time.sleep(1)
buf=camera.capture()
camera.deinit()
led.off()
