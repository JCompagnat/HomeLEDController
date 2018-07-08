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
vert.start(0)
bleu.start(0)
blanc.start(0)


def ambiance():
    try:
        while 1:
            for dc in range(0, 101, 5):
                rouge.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(0, 101, 5):
                bleu.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(0, 101, 5):
                vert.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                rouge.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                bleu.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                vert.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    bleu.stop()
    blanc.stop()
    rouge.stop()
    vert.stop()
    GPIO.cleanup()

    return()
