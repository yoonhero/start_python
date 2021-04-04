import serial

arduino = serial.Serial(port='/dev/tty.usbserial-1410',
                        baudrate=9600, timeout=None)


while True:
    c = input()
    if c == 'q':
        break
    else:
        arduino.serial(c)
