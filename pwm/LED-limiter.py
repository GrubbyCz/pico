from machine import Pin, ADC, PWM
import time

potentiometer = ADC(Pin(26))

led_pwms = [PWM(Pin(i)) for i in range(2, 10)]
for pwm in led_pwms:
    pwm.freq(1000)

num_leds = len(led_pwms)

def led_counting_pwm():
    blink_state = False  
    last_blink = time.ticks_ms()

    while True:
        pot_value = potentiometer.read_u16()
        exact_position = (pot_value / 65535) * num_leds
        full_leds = int(exact_position)
        partial_brightness = exact_position - full_leds

        if full_leds >= num_leds and partial_brightness == 0:
            if time.ticks_diff(time.ticks_ms(), last_blink) > 50:
                blink_state = not blink_state
                last_blink = time.ticks_ms()

            for pwm in led_pwms:
                pwm.duty_u16(65535 if blink_state else 0)

        else:
            for i, pwm in enumerate(led_pwms):
                if i < full_leds:
                    pwm.duty_u16(65535)
                elif i == full_leds:
                    pwm.duty_u16(int(partial_brightness * 65535))
                else:
                    pwm.duty_u16(0)

        print(f"Pozice: {exact_position:.2f}, Plných LED: {full_leds}, Částečný jas: {partial_brightness:.2f}")
        time.sleep(0.05)

led_counting_pwm()
