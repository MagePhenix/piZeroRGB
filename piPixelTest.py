from neopixel import NeoPixel
import board
from time import sleep

pixels = NeoPixel(board.D18, 59, auto_write=False, bpp=4)


colors = [(255,0,0,0), (0,255,0,0), (0,0,255,0), (0,0,0,255)]

while True:

    for i in range(3):
        pixels.fill(colors[i])
        pixels.show()
        print(pixels[0])
        sleep(2)