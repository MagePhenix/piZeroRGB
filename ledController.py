from collections import defaultdict
from typing import List
import colorCycle, colorManagement, serial, time, board
from neopixel import NeoPixel

class serialMonitor:

    def __init__(self, minCheckTime: int = 100) -> None:
        self.__lastChecked = time.thread_time_ns() - (1000000 * minCheckTime)
        self.__minDelay = minCheckTime
        self.__ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        self.__data = defaultdict(None)

    def readSerial(self, input: str = '0') -> dict:

        #ensure that data is not being requested too often
        if ((((time.time_ns() - self.__lastChecked) / 1000000) < self.__minDelay)):
            return self.__data

        #set the last checked time to current
        self.__lastChecked = time.time_ns()

        #send request for data
        self.__ser.write(input.encode('utf-8'))

        #read data
        rawData = self.__ser.read_until()

        #transform data into array
        dataArr = rawData.decode("utf-8").split(',')[:-1]

        #process data into dictonary
        for i in dataArr:
            name,value = i.split(':')[:2]

            self.__data[name] = value

        print(self.__data)
        return self.__data

inputs = serialMonitor()

class ledController:

    def __init__(self, ) -> None:
        self.__pixels = NeoPixel(board.D18, 118, auto_write=False, bpp=4)

        self.__modes = [

            self.__colorCycle,
            self.__solidcolor
        ]

        self.__updateIndex = 0

        self.__inputData = inputs.readSerial()

        self.__solidWhite = 0

    def update(self) -> None:
        
        #read in inputs
        self.__inputData = inputs.readSerial()

        #change mode if the first button is pressed
        if bool(self.__inputData['button0']):
            self.__updateIndex = (self.__updateIndex + 1) % len(self.__modes) 

        #run the update function
        self.__modes[self.__updateIndex]()



    def __colorCycle(self) -> None:
        pass

    def __solidFading(self) -> None:
        pass

    def __solidcolor(self) -> None:
        
        #turns the white on or off
        if self.__inputData["button3"]:
            self.__solidWhite = (self.__solidWhite + 1) % 2

        #empty array to store color
        color = []

        #add rgb colors
        for i in range(2, -1, -1):
            color.append(float(self.__inputData[f"pot{i}"]) * 255)
        
        color.append(255 * self.__solidWhite)

        self.__pixels.fill(color)

leds = ledController()

while True:

    leds.update()





