import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import board
import digitalio
import time

kbd = Keyboard(usb_hid.devices)

buttons = [
    digitalio.DigitalInOut(board.GP6),
    digitalio.DigitalInOut(board.GP5),
    digitalio.DigitalInOut(board.GP4),
    digitalio.DigitalInOut(board.GP3),
    digitalio.DigitalInOut(board.GP2),
    digitalio.DigitalInOut(board.GP1),
    digitalio.DigitalInOut(board.GP8),
    digitalio.DigitalInOut(board.GP0),
    digitalio.DigitalInOut(board.GP9),
    digitalio.DigitalInOut(board.GP7)
    ]

for button in buttons:
    button.switch_to_input(pull=digitalio.Pull.UP)

    jogMode = False
while True:
    press = False
    sideButton = not buttons[9].value
    
    if not buttons[0].value:    # X Axis  --> Row 0
        if sideButton:
            kbd.send(Keycode.CONTROL, Keycode.ONE)
        else:
            kbd.send(Keycode.SHIFT, Keycode.CONTROL, Keycode.X)
        press = True
        jogMode = True
    elif not buttons[1].value:  # Y Axis
        if sideButton:
            kbd.send(Keycode.CONTROL, Keycode.TWO)
        else:
            kbd.send(Keycode.SHIFT, Keycode.CONTROL, Keycode.Z)
        press = True
        jogMode = True
    elif not buttons[2].value:  # Z Axis
        if sideButton:
            kbd.send(Keycode.CONTROL, Keycode.THREE)
        else:
            kbd.send(Keycode.SHIFT, Keycode.CONTROL, Keycode.Y)
        press = True
        jogMode = True
    elif not buttons[3].value:  # 1mm     --> Row 1
        kbd.send(Keycode.CONTROL, Keycode.N)
        press = True
        jogMode = True
    elif not buttons[4].value:  # 10mm
        kbd.send(Keycode.CONTROL, Keycode.O)
        press = True
        jogMode = True
    elif not buttons[5].value:  # 100mm
        kbd.send(Keycode.CONTROL, Keycode.P)
        press = True
        jogMode = True
    elif not buttons[6].value:  #start    --> Row 2
        if sideButton:
            kbd.send(Keycode.CONTROL, Keycode.G)
            press = True
    elif not buttons[7].value:  # 0.1mm
        if jogMode:
            jogMode = False
            kbd.send(Keycode.F12)
            time.sleep(0.5)
            kbd.send(Keycode.F4)
            
        press = True
    elif not buttons[8].value:  #stop
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.G)
        press = True
#    elif not buttons[9].value:  # side button
#        kbd.send(Keycode.E)
#        press = True
        
    if press:
        time.sleep(0.2)
