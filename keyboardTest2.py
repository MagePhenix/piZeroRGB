import keyboard
from time import sleep
from customThreading import ThreadController


def sampleFunction1():
    print("1", end="")
    sleep(.1)

def sampleFunction2():
    print("2", end="")
    sleep(.1)

def sampleFunction3():
    print("3", end="")
    sleep(.1)

def sampleFunction4():
    print("4", end="")
    sleep(.1)


class keyManager:

    def __init__(self, keyMap: dict) -> None:
        self.keyMap = keyMap

        self.__threadManager = ThreadController()

    def awaitKey(self):
        """
        Waits for a key press and runs the associated funciton
        """

        key = keyboard.read_event(True)
        isNumpad = 0

        #fails out if there is no mapping or the key is being pressed initially
        if (key.name not in self.keyMap.keys()) | (key.event_type == "down"):
            return

        #sets whether the key is on the numpad or not
        if key.is_keypad:
            isNumpad = 1

        print("\n-----------------")


        #gets function list from dictionary
        functList = self.keyMap[key.name]
        #gets function from map
        newFunct = functList[isNumpad % len(functList)]

        #calls thread manager to start new thread
        self.__threadManager.startNewThrd(newFunct)

    def exit(self):
        """
        closes any running threads
        """

        self.__threadManager.endThrd()
        

keyMappings = {
    '1':[sampleFunction1],
    '2':[sampleFunction2, sampleFunction3],
    'c':[sampleFunction4]
}


print("Start")
keyWatch = keyManager(keyMappings)

for i in range(20):
    keyWatch.awaitKey()

keyWatch.exit()

print("Exit")





# while True:

#     key = keyboard.read_event(True)
#     print(f"{key.event_type} -- {key.name}")
#     if key.name == 'esc':
#         break