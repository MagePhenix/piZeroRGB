from time import sleep,time
from colorCycle import colorCycle
from neopixel import NeoPixel
import board


rgbCycle = colorCycle(["red", "green", "blue"], .1, 3, 15, brightness=.4)

pixels = NeoPixel(board.D18, 118, auto_write=False, bpp=4)

endTime = 5 + time()
count = 0

while time() < endTime:

    step = rgbCycle.getStep()

    for i in range(len(pixels)):

        pixels[i] = step[i % len(step)]

    pixels.show()
    count += 1

rgbCycle.switchDirection()
print(count)

while True:

    step = rgbCycle.getStep()

    for i in range(len(pixels)):

        pixels[i] = step[i % len(step)]

    pixels.show()