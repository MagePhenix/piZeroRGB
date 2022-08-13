import serial
import time


class serialMonitor:

    def __init__(self) -> None:
        self.lastChecked = time.time_ns() - (1000000 * 100)
        self.ser = serial.Serial('/dev/serial0', 1152000, timeout=1)
        self.data = ""

    def getValues(self, input = '0'):
        if ((time.time_ns() - self.lastChecked) / 1000000) < 100:
            return self.data

        # self.ser.write(input.encode('utf-8'))

        self.ser.flush()
        input = self.ser.readline()
        inputArr = input.decode("utf-8")[:-2].split(',')

        return inputArr

mon = serialMonitor()

ser = serial.Serial('/dev/serial0', 1152000, timeout=1)

end = time.time() + .1

while True:

    if(time.time() > end):
        print(ser.read_until().decode("utf-8"))
        end = time.time() + .1
