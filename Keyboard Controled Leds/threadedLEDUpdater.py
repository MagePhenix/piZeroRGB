from colorCycle import colorCycle
from neopixel import NeoPixel
import board

class ledUpdater:

    def __init__(self, pixels: NeoPixel) -> None:
        self.__cycle = None
        self.whiteBrightness = 0
        self.__brightness = 1

        self.__pixels = pixels

    def setLeds(self):

        step = self.__cycle.getStep(whiteValue=self.whiteBrightness)

        for i in range(len(self.__pixels)):
            self.__pixels[i] = step[i % len(step)]

        self.__pixels.show()

    def changePallett(self, cycle: colorCycle):
        """
        Switches to a different color cycle
        """

        cycle.brightness = self.__brightness

        self.__cycle = cycle

    def setBrightness(self, brighness: float = 1):
        """
        sets the Brightness of the led strips
        """

        if (brighness >= 0) & (brighness <= 1):
            self.__brightness = brighness
            self.__cycle.brightness = self.__brightness

    def getBrightness(self):
        return self.__brightness