import keyboard


# keysDict = {
#     'esc': 1, 
#     'f1': 59, 
#     'f2': 60, 
#     'f3': 61, 
#     'f4': 62, 
#     'f5': 63, 'f6': 64, 'f7': 65, 'f8': 66, 'f9': 67, 'f10': 68, 'f11': 87, 'f12': 88, 'print screen': 55, 'scroll lock': 70, 'pause': 69, 'stop media': -178, 'previous track': -177, 'play/pause media': -179, 'next track': -176, '`': 41, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, '0': 11, '-': 12, '=': 13, 'backspace': 14, 'insert': 82, 'home': 71, 'page up': 73, 'delete': 83, 'end': 79, 'page down': 81, 'tab': 15, 'q': 16, 'w': 17, 'e': 18, 'r': 19, 't': 20, 'y': 21, 'u': 22, 'i': 23, 'o': 24, 'p': 25, '[': 26, ']': 27, '\\': 43, 'caps lock': 58, 'a': 30, 's': 31, 'd': 32, 'f': 33, 'g': 34, 'h': 35, 'j': 36, 'k': 37, 'l': 38, ';': 39, "'": 40, 'enter': 28, 'shift': 42, 'z': 44, 'x': 45, 'c': 46, 'v': 47, 'b': 48, 'n': 49, 'm': 50, ',': 51, '.': 52, '/': 53, 'right shift': 54, 'ctrl': 29, 'left windows': 91, 'alt': 56, 'space': 57, 'right alt': 56, 'right windows': 92, 'menu': 93, 'right ctrl': 29, 'left': 75, 'down': 80, 'right': 77, 'up': 72, 'numnum lock': 69, 'num/': 53, 'num*': 55, 'num-': 74, 'numhome': 71, 'numup': 72, 'numpage up': 73, 'numleft': 75, 'numclear': 76, 'numright': 77, 'numend': 79, 'numdown': 80, 'numpage down': 81, 'numinsert': 82, 'numdelete': 83, 'numenter': 28, 'num+': 78}

# for k in keysDict.keys():
#     print(f"'{k}' : {keysDict[k]},")

# with open("keyConversions.txt", 'wt') as f:

#     for k in keysDict.keys():
#         print(f"'{k}' : {keysDict[k]},")
#         f.write(f"'{k}' : {keysDict[k]},\n")

while True:

    key = keyboard.read_event(True)

    if (key.scan_code == 1):
        break

    if (key.event_type == "up"):
        # print(f"{key.name}--{key.scan_code}--IsNumpad={key.is_keypad}")

        keyName = ('num' if key.is_keypad else "") + key.name
        print(f"'{keyName}' : {key.scan_code},")

        # keysDict[('num' if key.is_keypad else "") + key.name] = key.scan_code

# print(keysDict)
