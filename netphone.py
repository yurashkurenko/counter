import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#print(sta_if.scan())                             # Scan for available access points
sta_if.connect("OnePlus 8 Pro", "n6ggk5gs") # Connect to an AP
print(sta_if.ifconfig())
#print(sta_if.isconnected())                      # Check for successful connection
# Change name/password of ESP8266's AP:
#ap_if = network.WLAN(network.AP_IF)
#ap_if.config(ssid="<AP_NAME>", security=network.AUTH_WPA_WPA2_PSK, key="<key>")