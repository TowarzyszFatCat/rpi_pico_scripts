import time
from time import sleep
import digitalio
import board
import usb_hid
import adafruit_matrixkeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

onled = digitalio.DigitalInOut(board.GP9)
onled.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP8)
led2.direction = digitalio.Direction.OUTPUT


led.value = False
led2.value = False
onled.value = True

cols = [digitalio.DigitalInOut(x) for x in (board.GP5, board.GP6, board.GP7)]
rows = [digitalio.DigitalInOut(x) for x in (board.GP1, board.GP2, board.GP3, board.GP4)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

on = True

while True:
    keys = keypad.pressed_keys
    if keys:
        print(keys)
        if on == True:
            if keys == [1]:
                led2.value = False
                keyboard.press(Keycode.F11)
                led.value = True
                keyboard.release(Keycode.F11)
                sleep(0.1)
                led.value = False
                print("F11")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [2]:
                led2.value = False
                keyboard.press(Keycode.F12)
                led.value = True
                keyboard.release(Keycode.F12)
                sleep(0.1)
                led.value = False
                print("F12")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [3]:
                led2.value = False
                keyboard.press(Keycode.F13)
                led.value = True
                keyboard.release(Keycode.F13)
                sleep(0.1)
                led.value = False
                print("F13")
                led2.value = True
                time.sleep(0.5)
                led2.value = False

            elif keys == [4]:
                led2.value = False
                keyboard.press(Keycode.F14)
                led.value = True
                keyboard.release(Keycode.F14)
                sleep(0.1)
                led.value = False
                print("F14")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [5]:
                led2.value = False
                keyboard.press(Keycode.F15)
                led.value = True
                keyboard.release(Keycode.F15)
                sleep(0.1)
                led.value = False
                print("F15")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [6]:
                led2.value = False
                keyboard.press(Keycode.F16)
                led.value = True
                keyboard.release(Keycode.F16)
                sleep(0.1)
                led.value = False
                print("F16")
                led2.value = True
                time.sleep(0.5)
                led2.value = False

            elif keys == [7]:
                led2.value = False
                keyboard.press(Keycode.F17)
                led.value = True
                keyboard.release(Keycode.F17)
                sleep(0.1)
                led.value = False
                print("F17")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [8]:
                led2.value = False
                keyboard.press(Keycode.F18)
                led.value = True
                keyboard.release(Keycode.F18)
                sleep(0.1)
                led.value = False
                print("F18")
                led2.value = True
                time.sleep(0.5)
                led2.value = False
            elif keys == [9]:
                led2.value = False
                keyboard.press(Keycode.F19)
                led.value = True
                keyboard.release(Keycode.F19)
                sleep(0.1)
                led.value = False
                print("F19")
                led2.value = True
                time.sleep(0.5)
                led2.value = False

            elif keys == ["*"]:
                led2.value = False
                keyboard.press(Keycode.F21)
                led.value = True
                keyboard.release(Keycode.F21)
                sleep(0.1)
                led.value = False
                print("F21")
                led2.value = True
                time.sleep(0.5)
                led2.value = False

            elif keys == [0]:
                led2.value = False
                keyboard.press(Keycode.F20)
                led.value = True
                keyboard.release(Keycode.F20)
                sleep(0.1)
                led.value = False
                print("F20")
                led2.value = True
                time.sleep(0.5)
                led2.value = False

        if keys == ["#"]:

            if on == True:
                led2.value = False
                led.value = True
                sleep(0.1)
                led.value = False
                on = False
                onled.value = False
                led2.value = True
                time.sleep(0.5)
                led2.value = False

            elif on != True:
                led2.value = False
                led.value = True
                sleep(0.1)
                led.value = False
                on = True
                onled.value = True
                led2.value = True
                time.sleep(0.5)
                led2.value = False

    time.sleep(0.1)
print("Zakonczono")
