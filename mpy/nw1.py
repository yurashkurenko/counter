import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#print(sta_if.scan())                             # Scan for available access points
sta_if.connect("MERCUSYS_EB85", "n6ggk5gs") # Connect to an AP
print(sta_if.ifconfig())
