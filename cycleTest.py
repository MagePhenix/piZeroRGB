from colorCycle import colorCycle
from neopixel import NeoPixel
import board


rgbCycle = colorCycle(["red", "green", "blue"], 2, 5, 10, brightness=.4)

pixels = NeoPixel(board.D18, 59, auto_write=False, bpp=4)

while True:

    step = rgbCycle.getStep()

    for i,p in enumerate(pixels):

        p = step[i % len(step)]

    pixels.show()
