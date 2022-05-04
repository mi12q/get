import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

GPIO.output(troyka, 1)

GPIO.output(leds, 0)


def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def funcForLeds(value):
    resValue = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        if value - 32 <= 255 / 8 * i:
            resValue[i] = 1
    print(resValue)
    return resValue


def adc1():
    for value in range(256):
        signal = decToBin(value)

        GPIO.output(dac, signal)

        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            print(value)
            return value


def adc2():
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
        valueADS = adc2()
        voltageADS = valueADS / 256 * 3.3
        GPIO.output(leds, funcForLeds(256 - valueADS))
        print("Цифровое значение {:^3} -> {}, voltage = {:.2f}".format(valueADS, decToBin(valueADS), voltageADS))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()