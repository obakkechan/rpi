import RPi.GPIO as GPIO # GPIOからデジタル入出力するライブラリ

LED_PIN = 14    # GPIOの14番を使用する。

GPIO.setmode(GPIO.BCM)  # GPIOの番号で指定するモードに設定する。
GPIO.setup(LED_PIN, GPIO.OUT)   # LED_PINで指定した番号を、出力モードに設定する。

GPIO.output(LED_PIN, GPIO.HIGH) # LED_PINで指定した番号の出力を、High(3.3V)にする。