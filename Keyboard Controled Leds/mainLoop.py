from keyboardControl import keyBoardControlledLEDs


leds = keyBoardControlledLEDs

while True:
    keyBoardControlledLEDs.updateByKey()