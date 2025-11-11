from machine import Pin, UART
import time

# UART nastavení (UART0 = GP0, GP1)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Tlačítko na GP15
button = Pin(15, Pin.IN, Pin.PULL_UP)

prev_state = button.value()

while True:
    state = button.value()
    if state != prev_state:
        if state == 0:
            uart.write("BTN:1\n")
            print("Tlačítko stisknuto")
        else:
            uart.write("BTN:0\n")
            print("Tlačítko uvolněno")
        prev_state = state
    time.sleep(0.05)