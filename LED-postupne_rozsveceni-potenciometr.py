from machine import Pin, ADC
import time
potentiometer = ADC(Pin(26))

led_pins = [Pin(i, Pin.OUT) for i in range(2, 10)]
num_leds = len(led_pins)

def map_range(value, in_min, in_max, out_min, out_max):

    return int((value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)

def led_counting_digital():
    while True:
        pot_value = potentiometer.read_u16()

        active_leds = map_range(pot_value, 0, 65535, 0, num_leds)

        for i, led in enumerate(led_pins):
            led.value(1 if i < active_leds else 0)

        percent = (pot_value / 65535) * 100
        print(f"Pot: {pot_value} ({percent:.1f}%), LED: {active_leds}/{num_leds}")
        time.sleep(0.1)

led_counting_digital()
