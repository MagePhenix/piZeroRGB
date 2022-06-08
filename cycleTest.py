from time import sleep
from colorCycle import colorCycle
from neopixel import NeoPixel
import board


rgbCycle = colorCycle(["red", "green", "blue"], 1, 3, 7, brightness=.4)

pixels = NeoPixel(board.D18, 59, auto_write=False, bpp=4)

while True:

    step = rgbCycle.getStep()

    for i in range(len(pixels)):

        pixels[i] = step[i % len(step)]

    pixels.show()
