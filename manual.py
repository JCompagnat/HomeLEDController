import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

bleu=GPIO.PWM(5,120)

vert=GPIO.PWM(22,120)

rouge=GPIO.PWM(27,120)

blanc=GPIO.PWM(8,120)

rouge.start(0)
vert.start(100)
bleu.start(0)
blanc.start(0)

input('press key to stop: ')

bleu.stop()
blanc.stop()
rouge.stop()
vert.stop()
GPIO.cleanup()
