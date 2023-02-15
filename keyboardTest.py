from pynput.keyboard import Key, Listener

def test(key):
    print(F'{key}')

def keyReleased(key):
    if key == Key.esc:
        return False

with Listener(on_press=test,on_release=keyReleased) as listener:
    listener.join()