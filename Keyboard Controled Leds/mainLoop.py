from keyboardControl import keyBoardControlledLEDs


leds = keyBoardControlledLEDs

while True:
    leds.updateByKey()