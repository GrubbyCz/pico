import network
import time

w = network.WLAN(network.STA_IF)
w.active(True)
w.connect("Spur", "KanecDebil")

while not w.isconnected():
    time.sleep(0.1)

print("PICO IP:", w.ifconfig()[0])