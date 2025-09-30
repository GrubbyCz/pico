from machine import Pin, ADC, PWM
import time

# Inicializace potenciometru (na GP26)
potentiometer = ADC(Pin(26))

# LED na GP2, řízená přes PWM
led_pwm = PWM(Pin(2))
led_pwm.freq(1000)   # 1 kHz PWM (dostatečně rychlé, aby LED neblikala)

def basic_brightness_control():
    while True:
        # Přečteme hodnotu potenciometru (0–65535)
        pot_value = potentiometer.read_u16()
        
        # Nastavíme jas LED (stejný rozsah 0–65535)
        led_pwm.duty_u16(pot_value)
        
        # Pro ladění vypíšeme hodnoty do konzole
        brightness_percent = (pot_value / 65535) * 100
        print(f"Pot: {pot_value}, Jas: {brightness_percent:.1f}%")
        
        time.sleep(0.1)

# Spustíme hlavní smyčku
basic_brightness_control()
