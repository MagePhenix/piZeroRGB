import serial
import time


class serialMonitor:

    def __init__(self) -> None:
        self.lastChecked = time.time_ns() - (1000000 * 0)
        self.ser = serial.Serial('/dev/serial0', 1152000, timeout=1)
        self.data = ""

    def getValues(self, input = '0'):
        # self.ser.write(input.encode('utf-8'))

        self.ser.reset_input_buffer()
        data = self.ser.readline()
        inputArr = data.decode("utf-8")[:-2].split(',')

        self.data = inputArr

        return inputArr

mon = serialMonitor()

end = time.time() + .1

while True:

    if(time.time() > end):
        print(mon.getValues())
        end = time.time() + .1
