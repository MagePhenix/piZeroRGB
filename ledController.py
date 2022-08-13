from xmlrpc.client import Boolean
import colorCycle, colorManagement, serial, time, board
from neopixel import NeoPixel
from threading import Thread

class serialMonitor:

    def __init__(self, minCheckTime: int = 100) -> None:
        self.__lastChecked = time.thread_time_ns() - (1000000 * minCheckTime)
        self.__minDelay = minCheckTime
        self.__ser = serial.Serial('/dev/serial0', 1152000, timeout=1)
        self.__data = {}

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

class button:
    def __init__(self) -> None:
        self.__prevState = False
        self.val = False

    def getVal(self, newVal) -> Boolean:
        if ((newVal == "True") & (not self.__prevState)):
            self.__prevState = True
            self.val = True
        else:
            if newVal == "False":
                self.__prevState = False

            self.val = False

class pot:

    def __init__(self) -> None:
        self.val = 0

    def getVal(self, val) -> float:

        try:
            self.val = float(val)
        
        except:
            self.val = 0

def updateInputs():
    while True:
        global inputs
        inputs = serialPort.readSerial()

class ledController:

    def __init__(self, ) -> None:
        self.__pixels = NeoPixel(board.D18, 118, auto_write=False, bpp=4)

        self.__modes = [

            self.__colorCycle,
            self.__solidcolor
        ]

        self.__updateIndex = 0

        self.__solidWhite = 0

        self.__setInputs()

    def __setInputs(self):
        self.cleanedInputs = {}
        self.inputValues = {}

        for i in inputs.keys():
            if "pot" in i:
                self.cleanedInputs[i] = pot()
            else:
                self.cleanedInputs[i] = button()

    def __updateInputs(self):

        for i in inputs.keys():
            self.cleanedInputs[i].getVal(inputs[i])

    def update(self) -> None:

        self.__updateInputs()

        print(self.cleanedInputs['button0'].val)
        
        #change mode if the first button is pressed
        if self.cleanedInputs['button0'].val:
            self.__updateIndex = (self.__updateIndex + 1) % len(self.__modes) 

        #run the update function
        self.__modes[self.__updateIndex]()

        print(self.__updateIndex)



    def __colorCycle(self) -> None:
        pass

    def __solidFading(self) -> None:
        pass

    def __solidcolor(self) -> None:
        
        #turns the white on or off
        if self.cleanedInputs["button3"].val:
            self.__solidWhite = (self.__solidWhite + 1) % 2

        #empty array to store color
        color = []

        #add rgb colors
        for i in range(2, -1, -1):
            color.append(self.cleanedInputs[f"pot{i}"].val * 255)
        
        color.append(255 * self.__solidWhite)

        self.__pixels.fill(color)

serialPort = serialMonitor()
inputs = serialPort.readSerial()

leds = ledController()

inputThrd = Thread(target=updateInputs)
inputThrd.start()

while True:

    leds.update()

    time.sleep(.1)

