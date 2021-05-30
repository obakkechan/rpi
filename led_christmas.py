# coding: UTF-8
import RPi.GPIO as GPIO # I/O from GPIO
import time 

# LED_PIN_A = 14    # Use GPIO no.14
# LED_PIN_B = 15
# LED_PIN_C = 18
LED_PIN = [14, 15, 18]

cycle_term = 1
PWM_range = 100
# term = cycle_term / PWM_range
term = 0.01

hertz = 50
pwmout = []

GPIO.setmode(GPIO.BCM)  # Set using GPIO no. mode

for PIN in LED_PIN:
    GPIO.setup(PIN, GPIO.OUT)   # Set GPIO output mode
    pwmout.append(GPIO.PWM(PIN, hertz))
for pwm in pwmout:
    pwm.start(0)

while(True):
    x = 0
    for x in range(PWM_range):
        # pwm_duty=[100*(1-(x/PWM_range)),0,0]
        pwm_duty=[100-x,0,0]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)
        
    x = 0
    for x in range(PWM_range):
        pwm_duty=[0,100-x,0]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)

    x = 0
    for x in range(PWM_range):
        pwm_duty=[0,0,100-x]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)

    x = 0
    for x in range(PWM_range):
        pwm_duty=[100-x,100-x,0]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)

    x = 0
    for x in range(PWM_range):
        pwm_duty=[0,100-x,100-x]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)
        
    x = 0
    for x in range(PWM_range):
        pwm_duty=[100-x,0,100-x]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)





    x = 0
    for x in range(PWM_range):
        pwm_duty=[100-x,100-x,100-x]
        LED_team=0
        for pwm in pwmout:
            pwm.ChangeDutyCycle(pwm_duty[LED_team])
            LED_team += 1
        time.sleep(term)

for pwm in pwmout:
    pwm.stop()
