import keyboard
from threading import Thread
from time import sleep


keyMappings = {
    'a':[print],
    'b':[],
    'c':[],
    'esc':[]
}

class keyControlledThrd:

    def __init__(self) -> None:
        """
        Sets up thread variables
        """

        #flag for the thread
        self.keepRunning = False
        
        #creates initial thread object
        self.t1 = Thread(target=(self.__threadRunner), args=(None,))
        #starts first thread
        self.t1.start()

    def __threadRunner(self, funct):
        """
        Runs function until keepRunning is set to false
        """
        while self.keepRunning:
            funct()

    def startNewThrd(self, funct):
        """
        Stops previous thread and runs new function
        """

        #checks to make sure a function was passed
        if not callable(funct):
            return

        #flags thread to stop
        self.keepRunning = False

        #waits for the thread to end
        self.t1.join()

        #resets thread flag
        self.keepRunning = True

        #creates new thread with function
        self.t1 = Thread(target=(self.__threadRunner), args=(funct,))

        #runs new thread
        self.t1.start()

    def endThrd(self):
        """
        Stops running thrd
        """
        self.keepRunning = False
        self.t1.join()
        

print("Starting...")

ledString = keyControlledThrd()

ledString.startNewThrd(print)

sleep(.001)

ledString.endThrd()

print("Done")





# while True:

#     key = keyboard.read_event(True)
#     print(f"{key.event_type} -- {key.name}")
#     if key.name == 'esc':
#         break