import uos
import machine
import time
led = machine.Pin(4, machine.Pin.OUT)
import camera
led.on()
camera.init(0, format=camera.JPEG, fb_location=camera.DRAM)
buf=camera.capture()
camera.deinit()
led.off()
