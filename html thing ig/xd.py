from pynput.mouse import Listener, Button, Controller
from pynput import keyboard
import time
import threading

stop = True

def presser():
    global stop
    mouse = Controller()
    while True:
        print(stop)
        if stop == False:
            mouse.click(Button.left, 1)
            time.sleep(.05)
        else:
            return 0


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    global stop
    print('{0} released'.format(
        key))

    if key == keyboard.Key.page_down:
        print(str(stop)+"111")
        if stop == True:
            global t
            stop = False
            t = threading.Thread(target=presser)
            t.start()
            
        else:
            stop == True
    if key == keyboard.Key.page_up:
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

