def hexToRGB(hexValue: str):
    """
    Takes a HEX color code and returns RGB values
    """
    
    #removes '#' from string
    hexValue = hexValue.strip("#")
    #converts each pair of charactersin the string to int
    rgbValues = [int(hexValue[i:i+2], 16) for i in range(0, len(hexValue), 2)]

    #returns the first three values from the list
    return rgbValues[0], rgbValues[1], rgbValues[2]

def colorToHex(color: str):
    """
    A color and it to a hexString
    """
    
    color = color.lower()

    #dictonary of colors by name
    colors = {

    #8 canonical colors
    "red":"#ff0000",
    "yellow":"#ffff00",
    "green":"#00ff00",
    "cyan":"#00ffff",
    "blue":"#0000ff",
    "violet":"#ff00ff",
    "white":"#ffffff",
    "black":"#000000",

    #custom colors
    "orange":"#ff5100",
    "sky":"#6bceff"
    }

    if color in colors:
        return colors[color]
    
    return None

def toRGB(color):
    """
    Tries to return RGB values from a passed value
    """

    #check if the color is alread three values
    if type(color) == tuple or type(color) == list:

        #make sure it hase three items
        if len(color) < 3:
            return None

        #caste to a list
        color = list(color)

        #convert to rgb values from string or reduce below 255
        for i, val in enumerate(color[:3]):
            if type(val) == str:
                color[i] = int(val[:2], 16)

            color[i] = int(color[i])

            if color[i] > 255:
                color[i] = 255
            if color[i] < 0:
                color[i] = 0

        return tuple(color[:3])

    #convert color name to hex
    if colorToHex(color):
        try:
            color = colorToHex(color)
        except:
            return None

    #convert hex to rgb values
    if (color[0] == "#") or (len(color) == 6):
        try:
            return hexToRGB(color)
        except:
            pass

    return None

def listToRGBList(colors: list, whiteVal: tuple = tuple([0])) -> tuple:
    """
    Returns a tuple of tuples of rgb values
    """
    
    #sets up return list
    rgbValues = []
    

    #tries to convert all the colors
    for val in colors:

        color = toRGB(val)

        if color:
            rgbValues.append(color + whiteVal)

    return tuple(rgbValues)