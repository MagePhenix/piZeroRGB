from customThreading import ThreadController
from keyboard import read_event as kbEvent
from colorCycle import colorCycle
from threadedLEDUpdater import ledUpdater
from neopixel import NeoPixel
import board

class keyBoardControlledLEDs:
    
    def __init__(self, stringLength: int = 177) -> None:

        #creates thread manager
        self.__threadManager = ThreadController()

        #the most recently pressed key
        self.__pressedKey = None

        #neo pixel string
        self.__pixels = NeoPixel(board.D18, stringLength, auto_write=False, bpp=4)

        #what function each key maps to
        self.__keyMap = {
            'num0' : self.__selectPallett,
            'num-' : self.__updateBrightness,
            'num+' : self.__updateBrightness,
            'numenter' : self.__toggleOnOff

        }

        #all the color cycles that can be called
        self.__colorCycles = [
            colorCycle(["red", "green", "blue"], .1, 15, 15, brightness=.2),
            colorCycle(["#FF5400","#6B4AFF","#00FFB8"], .1, 10, 50, brightness=.2),
            colorCycle(["#FF00AA","#2000FF","#FF0030"], .1, 10, 50, brightness=.1),
            colorCycle(["#3030FF","#FF0099","#DDDDDD", "FF0099", "3030FF"], .1, 5, 10, brightness=.2),
            colorCycle(["#3300FF","#202080","#FF00D0", "#0000FF"], .1, 0, 40, brightness=.2),
            colorCycle(["#00FF00","#00FFA8","#50FF00"], .1, 20, 20, brightness=.2),
            colorCycle(["#00FF00","#FF6600","#00ff80"], .1, 5, 30, brightness=.2)
        ]

        #tracks the current cycle in use
        self.__currentCycleIndex = 0

        #object for threaded led updating
        self.__ledUpdater = ledUpdater(self.__pixels)

        #stores led brightness
        self.__ledBrigthness = .1

    def updateByKey(self):
        """
        Waits for a valid key press and runs appropriate function in response
        """

        #gets keypress
        self.__awaitValidKeyRelease()

        #runs appropriate function
        self.__keyMap[self.__pressedKey]()

    def __awaitValidKeyRelease(self):
        """
        Loops until a key in the key map is released
        """
        
        while True:

            #waits for a keybaord event to occur
            key = kbEvent(True)

            #exits the loop when a key in the key map is released
            if (key.event_type == "up") & ((("num" if key.is_keypad else "") + key.name) in self.__keyMap.keys()):
                break

        #sets pressed key value
        self.__pressedKey = ("num" if key.is_keypad else "") + key.name

    def __selectPallett(self):
        """
        Sets a pallett and sets it to run in another thread
        """

        #iterates to the next cycle index
        self.__currentCycleIndex = (self.__currentCycleIndex + 1) % len(self.__colorCycles)

        self.__ledUpdater.changePallett(self.__colorCycles[self.__currentCycleIndex])

        if not self.__threadManager.keepRunning:
            self.__threadManager.startNewThrd(self.__ledUpdater.setLeds)

    def __updateBrightness(self, value: float = None):

        #sets the brightness by value
        if value is not None:
            self.__ledUpdater.setBrightness(value)
            return

        #if not increments the brightness
        value = .1

        if self.__pressedKey == 'num-': sign = -1
        elif self.__pressedKey == 'num+' : sign = 1

        self.__ledUpdater.setBrightness(self.__ledUpdater.getBrightness() + (value * sign))

        self.__ledBrigthness = self.__ledUpdater.getBrightness()

    def __toggleOnOff(self):

        #stops thrd
        self.__threadManager.endThrd()

        #clears pixels
        self.__pixels.fill([0,0,0,0])
        self.__pixels.show()

        #stores the value for this function in the map
        onOffKey = self.__pressedKey


        while True:
            self.__awaitValidKeyRelease()
            if self.__pressedKey == onOffKey:
                break

        #restarts thrd
        self.__threadManager.repeatLastThrd()


