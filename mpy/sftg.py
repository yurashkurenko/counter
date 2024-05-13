import ubinascii
import uos
import urequests
import random

boundary = ubinascii.hexlify(random(16)).decode('ascii')
print(boundary)
