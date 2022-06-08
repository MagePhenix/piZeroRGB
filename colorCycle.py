import imp
from locale import setlocale
from turtle import width
import colorManagement
from typing import List, Tuple
import time


class colorCycle:

    def __init__(self, colors: List, cycleTime: int = 1, width: int = 1, step: int = 1, brightness:float = 1) -> None:
        self.__colorList = colorManagement.listToRGBList(colors)
        self.cycleTime = cycleTime
        self.__width = width
        self.__step = step
        self.__colorCycle = []
        self.__buildColorCycle()
        self.__cycleLenth = len(self.__colorCycle)
        self.brightness = brightness

        self.__index = 1
        self.__endTime = time.time()

    def __buildColorCycle(self)  -> None:
        """
        Sets up initial color loop
        """

        #Loop through all the colors
        for i,c in enumerate(self.__colorList):
            
            #Add each solid color
            self.__colorCycle = list(self.__colorCycle + ([c] * self.__width))

            #Add intermediate colors
            for j in range(self.__step):
                
                color = []

                percent = (1 / (self.__step + 1)) * (j + 1)

                currentColor = c
                nextColor = self.__colorList[(i + 1) % len(self.__colorList)]
                
                #Loop over RGB values
                for k in range(3):

                    #Interpolate between the two values
                    color.append(int(currentColor[k] + ((nextColor[k] - currentColor[k]) * percent)))

                #add white value
                color.append(0)

                self.__colorCycle.append(tuple(color))

        self.__colorCycle = tuple(self.__colorCycle)
    
    def getStep(self, length:int = None, whiteValue:float = 0) -> List[Tuple]:
        """
        Returns a list of color values based on the internal percent
        """

        if not length:
            length = self.__cycleLenth

        #how far between transitions
        percent =  1 - ((self.__endTime - time.time()) / self.cycleTime)

        if percent >= 1:

            #increment the index
            self.__index = (self.__index - 1) % self.__cycleLenth

            #sets the time the the current step will end
            self.__endTime = time.time() + self.cycleTime

            #returns the colors for the start of the current step
            return [self.__colorCycle[(i % self.__cycleLenth)] for i in range(length - 1, -1, -1)]

        colorList = []

        #create a color list of the passed length
        for i in range(length):

            currentColor = self.__colorCycle[(i + self.__index) % self.__cycleLenth]
            nextColor = self.__colorCycle[(i + (self.__index + 1)) % self.__cycleLenth]

            rgbVals = []

            #loop over RGB
            for j in range(3):
                rgbVals.append(int((currentColor[j] + (percent * (nextColor[j] - currentColor[j]))) * self.brightness))

            #add white value
            rgbVals.append(whiteValue)

            #add the color to the list
            colorList.append(tuple(rgbVals))
                
        return colorList

# rgbCycle = colorCycle(["red", "blue"], 1, 3, 0, brightness=.4)

# while True:
#     rgbCycle.getStep()