from neopixel import NeoPixel
import board

pixels = NeoPixel(board.D18, 177, auto_write=False, bpp=4)

pixels.fill([0,0,0,0])

pixels.show()