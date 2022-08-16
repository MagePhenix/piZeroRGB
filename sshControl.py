from turtle import update
from colorCycle import colorCycle
# from neopixel import NeoPixel
import threading, Subclasses.stringUpdater, Subclasses.userInput


print("Building Pixel Maps...")
colorMaps = {

    "Rgb":colorCycle(["red", "green", "blue"], .1, 5, 30, brightness=1),
    "BluePink":colorCycle(["#ff0030", "#0000ff", "#ff030", "#5500ff"], .7, 3, 20, brightness=1)

}

print("Creating String...")
# pixels = NeoPixel(board.D18, 177, auto_write=False, bpp=4)

print("Running...")

mapFunction = colorMaps["Rgb"].getStep

Subclasses.stringUpdater.updateString()