ARDUINO_DIR            = /usr/share/arduino
TARGET                 = GroboticsCore
ARDUINO_LIBS           =
MCU                    = atmega328p
F_CPU                  = 16000000
ARDUINO_PORT           = /dev/ttyUSB0
AVRDUDE_ARD_BAUDRATE   = 57600
AVRDUDE_ARD_PROGRAMMER = arduino
BOARD_TAG              = nano

include /usr/share/arduino/Arduino.mk
