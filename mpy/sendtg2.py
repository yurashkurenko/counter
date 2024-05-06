# MicroPython v1.20.0-39-g61b8e1b2d-kaki5 on 2023-05-20; ESP32 CAMERA w/SSL (KAKI5) with ESP32
import machine
import camera
import time
import urequests

led = machine.Pin(4, machine.Pin.OUT)
camer.init()
led.on()
time.sleep(2)
buf=camera.capture()
led.off()
