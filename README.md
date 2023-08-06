# Deutsch
## Tom simple handrad für EdingCnc mit dem Rasberry-Pi Pico
### Grundfunktion:
  1.  Der Drehgeber wird direkt mit den Eingängen der Eding Anschlussplatine verbunden.
   * +5V 
   * GND
   * HANDWHEEL A
   * HANDWHEEL B
  2.  Der Notaus wird direkt mit der Steuerung verbunden, paralell zum normalen Notaus. Die Steuerung muss in dieser Konfiguration auf NO konfiguriert werden. 
   * ESTOP
   * GND
  3. Die 10 Funktionstasten des Handrades werden direkt mit den Eingängen des PiPico verbunden:

| Eingang | Funktion |
| --- |:-------------:|
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
   * Als Nächstes müssen die [Dateien](https://github.com/TheBlueManCoding/tshwEdingCnc/tree/main/src) im Repository auf das USB Laufwerk des PiPico kopiert werden (Hauptverzeichnis)
![Soll-Ordnerstruktur](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/67d1aaba23f07c7498afed532d94e842163adbea/img/FolderStructure.png)





![Handrad, Draufsicht](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Layout.jpg)
![Handrad, geöffnet](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Handrad_innen.jpg)

# English
## Tom simple handweel für EdingCnc using the Rasberry-Pi Pico
### Functionality:
  1.  The rotary encoder is directly connected to the inputs of the eding-cnc circuit board.
   * +5V 
   * GND
   * HANDWHEEL A
   * HANDWHEEL B
  2.  The emergency stop is connected in parallel to the other emergency stops. The controller input has to be configured to NO (normally-open). 
   * ESTOP
   * GND
  3. The 10 buttons of the handweel are directly connected to the picos input pins:

| input | function |
| --- |:-------------:|
| GP6 | X Axis |
| GP5 | Y Axis |
| GP4 | Z Axis |
| GP3 | 1mm/rotation |
| GP2 | 10mm/rotation |
| GP1 | 100mm/rotation |
| GP8 | start (green) |
| GP0 | automatic (leave the Jog-mode) |
| GP9 | stop (red) |
| GP7 | side-button |

The keys start and stop only work if pressed simultaneously with the side-button.

  4.  The keys of the handweel directly send inputs to the computer using the adafruit-hid libary. For that the Pico has to be directly connected to the PC via its USB connector and a micro-USB cable.
  5.  Preparation of the Pico:
   * Installation-process of Circuit-Python on the Pico: [Link](https://www.diyprojectslab.com/raspberry-pi-pico-with-circuitpython/)
   * Next the [Files](https://github.com/TheBlueManCoding/tshwEdingCnc/tree/main/src) from the Repository have to be copied to the drive of the Pico (root directory)
![example for a right set up pico](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/67d1aaba23f07c7498afed532d94e842163adbea/img/FolderStructure.png)





![Handwheel, closed](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Layout.jpg)
![Handwheel, opened](https://github.com/TheBlueManCoding/tshwEdingCnc/blob/main/img/Handrad_innen.jpg)
