from machine import Pin, UART
import time

# UART nastavení
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# LED na GP16
led = Pin(16, Pin.OUT)

buffer = b""

while True:
    if uart.any():
        data = uart.read().decode()
        buffer += data.encode()
        
        # zpracuj celý příkaz
        if "\n" in data:
            command = buffer.strip()
            buffer = b""
            
            if "BTN:1" in command:
                led.value(1)
                print("LED ON")
            elif "BTN:0" in command:
                led.value(0)
                print("LED OFF")
    time.sleep(0.05)