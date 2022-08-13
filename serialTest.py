import re
from sys import byteorder
import serial
import time


class serialMonitor:

    def __init__(self) -> None:
        self.lastChecked = time.time_ns() - (1000000 * 100)
        self.ser = serial.Serial('/dev/serial0', 115200, timeout=5)
        self.data = ""

    def getValues(self):
        if ((time.time_ns() - self.lastChecked) / 1000000) < 100:
            return self.data

        self.ser.write(1)

        input = self.ser.read_until()
        inputArr = input.decode("utf-8").split(',')

        return inputArr

mon = serialMonitor()

while True:

    input("Paused")

    print(mon.getValues())