import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#inner
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)
GPIO.cleanup()
