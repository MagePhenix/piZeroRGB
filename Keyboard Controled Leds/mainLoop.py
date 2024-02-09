from keyboardControlV2 import keyBoardControlledLEDs


leds = keyBoardControlledLEDs()

while True:
    leds.updateByKey()