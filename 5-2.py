import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 1)


def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    value = 0

    for i in reversed(range(8)):
        signal = decToBin(value + 2 ** i)
        GPIO.output(dac, signal)
        time.sleep(0.05)
        if (GPIO.input(comp) == 1):
            value += 2 ** i

    return value


try:
    while True:
        valueADS = adc()
        voltageADS = valueADS / 256 * 3.3
        print("Цифровое значение {:^3}, voltage = {:.2f}".format(valueADS, voltageADS))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()