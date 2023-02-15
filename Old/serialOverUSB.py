import time, serial

class serialMonitor:

    def __init__(self) -> None:
        self.lastChecked = time.time_ns() - (1000000 * 0)
        self.ser = serial.Serial('/dev/serial0', 1152000, timeout=1)
        self.data = ""

    def getValues(self, input = '0'):
        # self.ser.write(input.encode('utf-8'))

        data = self.ser.readline()
        inputArr = data.decode("utf-8")

        self.data = inputArr

        return inputArr

    def sendValues(self, input = "0"):

        self.ser.write(input.encode('utf-8'))


serPort = serialMonitor()

while True:

    info = serPort.getValues()
    
    serPort.sendValues(info)