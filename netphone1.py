import network
import time
sta_if = network.WLAN(network.STA_IF)
#time.sleep(5)
def connect():
    sta_if = network.WLAN(network.STA_IF)
    time.sleep(1)
    sta_if.active(True)
    time.sleep(1)
    sta_if.connect("OnePlus 8 Pro", "n6ggk5gs") # Connect to an AP
    time.sleep(1)
    print(sta_if.ifconfig())
    
def disconnect():
    sta_if.disconnect()
    time.sleep(1)
    print(sta_if.ifconfig())
    
#print(sta_if.scan())                             # Scan for available access points
#sta_if.connect("OnePlus 8 Pro", "n6ggk5gs") # Connect to an AP
#time.sleep(5)
#print(sta_if.ifconfig())
#print(sta_if.isconnected())                      # Check for successful connection
# Change name/password of ESP8266's AP:
#ap_if = network.WLAN(network.AP_IF)
#ap_if.config(ssid="<AP_NAME>", security=network.AUTH_WPA_WPA2_PSK, key="<key>")
