import keyboard


while True:

    key = keyboard.read_event(True)
    print(f"{key.event_type} -- {key.name}")
    if key.name == 'esc':
        break