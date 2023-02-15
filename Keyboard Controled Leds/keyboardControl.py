from customThreading import ThreadController
from keyboard import read_event as kbEvent
from colorCycle import colorCycle
from threadedLEDUpdater import ledUpdater

class keyBoardControlledLEDs:
    
    def __init__(self) -> None:

        #creates thread manager
        self.__threadManager = ThreadController()

        #the most recently pressed key
        self.__pressedKey = None

        #what function each key maps to
        self.__keyMap = {
            'num1' : self.__selectPallett,
            'num2' : self.__selectPallett,
            'num3' : self.__selectPallett,
            'num4' : self.__selectPallett,
            'num-' : self.__updateBrightness,
            'num+' : self.__updateBrightness,
            'num0' : self.__toggleOnOff

        }

        #what cycle each key maps to
        self.__cycleKeyMap = {
            'num1' : colorCycle(["red", "green", "blue"], .1, 3, 15, brightness=.2),
            'num2' : colorCycle(["#FF5400","#6B4AFF","#00FFB8"], .1, 10, 50, brightness=.2),
            'num3' : colorCycle(["#FF00AA","#2000FF","#FF0030"], .1, 10, 50, brightness=.1),
            'num4' : colorCycle(["#3030FF","#FF0099","#DDDDDD", "FF0099", "3030FF"], .1, 5, 10, brightness=.2),
        }

        #object for threaded led updating
        self.__ledUpdater = ledUpdater()

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

            print(key)

            #exits the loop when a key in the key map is released
            if (key.event_type == "up") & ((("num" if key.is_keypad else "") + key.name) in self.__keyMap.keys()):
                break

        #sets pressed key value
        self.__pressedKey = ("num" if key.is_keypad else "") + key.name

    def __selectPallett(self):
        """
        Sets a pallett and sets it to run in another thread
        """

        self.__ledUpdater.changePallett(self.__cycleKeyMap[self.__pressedKey])

        if not self.__threadManager.keepRunning:
            self.__threadManager.startNewThrd(self.__ledUpdater.setLeds)

    def __updateBrightness(self):

        value = .1

        if self.__pressedKey == 'num-': sign = -1
        elif self.__pressedKey == 'num+' : sign = 1

        self.__ledUpdater.setBrightness(self.__ledUpdater.getBrightness() + (value * sign))

    def __toggleOnOff(self):
        
        #stops thrd
        self.__threadManager.endThrd()

        #stores the value for this function in the map
        onOffKey = self.__pressedKey

        while True:
            self.__awaitValidKeyRelease()
            if self.__pressedKey == onOffKey:
                break

        #restarts thrd
        self.__threadManager.repeatLastThrd()