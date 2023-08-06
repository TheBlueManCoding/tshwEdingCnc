# Tom simple handrad für EdingCnc
## Grundfunktion:
  1.  Der Drehgeber wird direkt mit den Eingängen der Eding Anschlussplatine verbunden.
  * +5V 
  * GND
  * HANDWHEEL A
  * HANDWHEEL B
  2.  Der Notaus wird direkt mit der Steuerung verbunden, paralell zum normalen Notaus. Die Steuerung muss in dieser Konfiguration auf NO konfiguriert werden. 
  * ESTOP
  * GND
  3. Die 10 Funktionstasten des Handrades werden direkt mit den Eingängen des PiPico verbunden:

| Eingang        | Funktion |
| ------------- |:-------------:|
| GP6 | X Achse |
| GP5 | Y Achse |
| GP4 | Z Achse |
| GP3 | 1mm/Umdrehung |
| GP2 | 10mm/Umdrehung |
| GP1 | 100mm/Umdrehung |
| GP8 | Start (grün) |
| GP0 | Automatik (Verlassen des Jog-Modus) |
| GP9 | Stop (rot) |
| GP7 | Seitentaste |

Die Tasten Start und Stop funktionieren nur, wenn sie zusammen mit der Seitentaste gedrückt werden.

  4.  Die Tasten des Handrads senden per USB Tastatur-Befehle an die Software. Dazu wird der USB Anschluss des PiPico direkt mit dem PC verbunden.
  5.  Softwarevorbereitung:
  * Installation von Circuit-Python auf dem PiPico: [Link](https://www.elektronik-kompendium.de/sites/raspberry-pi/2706221.htm)
  * 






# Tom simple handwheel for EdingCnc

This software is written in CircuitPython for RP2040.

It uses the keyboard emulation and all the avaliable shortcuts in EdingCnc to get the buttons working.
The encoder is directly connected to the encoder input of the cpu board. The emergency stop is connected to one of the estop inputs.

As the RP2040 has enough input pins, every button is directly connected to one input and just switches the input to low. Its that simple.

To install the software just install CircuitPython onto your Raspberry. Then copy all files in the "src" of this repo onto the raspberry.

The current version uses inputs 0 to 9 - the order isn't straight as i did some mistakes in my hardware and fixed it in software.
But the pins are set up in a table and its easy to change the pinout.

![Handwheel](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Layout.jpg)
