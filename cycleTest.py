from time import sleep,time
from colorCycle import colorCycle
from neopixel import NeoPixel
import board


rgbCycle = colorCycle(["red", "green", "blue"], .1, 3, 15, brightness=.4)

pixels = NeoPixel(board.D18, 118, auto_write=False, bpp=4)

endTime = 10 + time()

while time() < endTime:

    step = rgbCycle.getStep()

    for i in range(len(pixels)):

        pixels[i] = step[i % len(step)]

    pixels.show()

rgbCycle.switchDirection()

while True:

    step = rgbCycle.getStep()

    for i in range(len(pixels)):

        pixels[i] = step[i % len(step)]

    pixels.show()