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
            'num1' : self.__updateBrightness,
            'num2' : self.__updateBrightness,
            'num3' : self.__updateBrightness,
            'num.' : self.__toggleWhite,
            'numenter' : self.__toggleOnOff

        }

        #all the color cycles that can be called
        self.__colorCycles = [
            #generic rainbow
            colorCycle(["red", "green", "blue"], .3, 20, 25),
            #very pink
            colorCycle(["#FF00AA","#2000FF","#FF0030"], .3, 10, 50),
            #trans
            colorCycle(["#3030FF","#FF0099","#DDDDDD", "FF0099", "3030FF"], .3, 5, 10),
            #mostly green
            colorCycle(["#00FF00","#00FFA8","#50FF00"], .3, 20, 20),
            #green cyan orange
            colorCycle(["#00FF00","#FF6600","#00ff80"], .3, 5, 30),
            #mostly blue orange
            colorCycle(["#0000AA", "#0000FF", "#0000FF", "#0000FF", "#0000AA", "#FF6600", "#0000AA", "#0000FF", "#0000AA""#FF3300"], cycleTime=.3, width=1, step=10),
            #blue green
            colorCycle(["blue", "blue", "green"], cycleTime=.3, width=30, step=20)
        ]

        #tracks the current cycle in use
        self.__currentCycleIndex = -1

        #object for threaded led updating
        self.__ledUpdater = ledUpdater(self.__pixels)

        #stores led brightness
        self.__ledBrigthness = 1

        #start the first cycle
        self.__selectPallett()

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

        if self.__pressedKey == 'num1': intensity = .1
        elif self.__pressedKey == 'num2' : intensity = .5
        elif self.__pressedKey == 'num3' : intensity = 1

        # self.__ledUpdater.setBrightness(self.__ledUpdater.getBrightness() + (value * sign))
        self.__ledUpdater.setBrightness(intensity)

        self.__ledBrigthness = self.__ledUpdater.getBrightness()

    def __toggleOnOff(self):
        """
        Stops everything until the strips are turned back on
        """

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

    def __toggleWhite(self):

        #stops thrd
        self.__threadManager.endThrd()

        #turns pixels white
        self.__pixels.fill((0, 0, 100, 150))
        self.__pixels.show()

        #stores the value for this function in the map
        toggleKey = self.__pressedKey

        while True:
            self.__awaitValidKeyRelease()
            if self.__pressedKey == toggleKey:
                break

        #restarts thrd
        self.__threadManager.repeatLastThrd()


