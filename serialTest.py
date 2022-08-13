import serial
import time


class serialMonitor:

    def __init__(self) -> None:
        self.lastChecked = time.time_ns() - (1000000 * 100)
        self.ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        self.data = ""

    def getValues(self, input = '0'):
        if ((time.time_ns() - self.lastChecked) / 1000000) < 100:
            return self.data

        self.ser.write(input.encode('utf-8'))

        input = self.ser.read_until()
        inputArr = input.decode("utf-8").split(',')[:-1]

        return inputArr

mon = serialMonitor()

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

while True:

    print(ser.read_until().decode("utf-8"))