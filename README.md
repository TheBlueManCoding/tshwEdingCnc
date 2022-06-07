# Tom simple handwheel for EdingCnc

This software is written in CircuitPython for RP2040.

It uses the keyboard emulation and all the avaliable shortcuts in EdingCnc to get the buttons working.
The encoder is directly connected to the encoder input of the cpu board. The emergency stop is connected to one of the estop inputs.

As the RP2040 has enough input pins, every button is directly connected to one input and just switches the input to low. Its that simple.

To install the software just install CircuitPython onto your Raspberry. Then copy all files in the "src" of this repo onto the raspberry.

The current version uses inputs 0 to 9 - the order isn't straight as i did some mistakes in my hardware and fixed it in software.
But the pins are set up in a table and its easy to change the pinout.

![Handwheel](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Layout.jpg)
