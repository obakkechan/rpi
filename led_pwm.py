# coding: UTF-8
import RPi.GPIO as GPIO # I/O from GPIO
import time 

LED_PIN = 14    # Use GPIO no.14
PWM_DUTY = 80   # Output ratio 0~100

GPIO.setmode(GPIO.BCM)  # Set using GPIO no. mode
GPIO.setup(LED_PIN, GPIO.OUT)   # Set the GPIO no. to output mode

pwmout = GPIO.PWM(LED_PIN, 50)  # Output in 50Hz PWM
pwmout.start(0)
pwmout.ChangeDutyCycle(80)    # Output PWM in PWM_DUTY
time.sleep(3)
pwmout.ChangeDutyCycle(20)    # Output PWM in PWM_DUTY
time.sleep(3)
pwmout.ChangeDutyCycle(80)    # Output PWM in PWM_DUTY
time.sleep(3)
pwmout.stop()   # Stop PWM output
