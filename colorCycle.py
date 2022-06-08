import time
from turtle import width
import colorManagement
from typing import List


class colorCycle:

    def __init__(self, colors: List, time: int = 1, width: int = 1, step: int = 1) -> None:
        self.colorList = colorManagement.listToRGBList(colors)
        self.cycleTime = time
        self.width = width
        self.step = step
        self.__buildColorList()

    def __buildColorCycle(self)  -> None:
        
        self.colorCycle = []

        #Loop through all the colors
        for i,c in enumerate(self.colorList):
            
            self.colorCycle += [c] * width


