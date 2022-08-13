from collections import defaultdict
import colorManagement
import serial
import time

class serialMonitor:

    def __init__(self, minCheckTime: int = 100) -> None:
        self.__lastChecked = time.thread_time_ns() - (1000000 * minCheckTime)
        self.__minDelay = minCheckTime
        self.__ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        self.__data = defaultdict(None)

    def readSerial(self, input: str = '0'):

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

        return self.__data

inputs = serialMonitor()

while True:

    time.sleep(2)

    print(inputs.readSerial())






