import serial,time

ser=serial.Serial()
ser.timeout=5
ser.port='COM7'
ser.baudrate=9600
ser.open()
time.sleep(1)
ser.flush()

ones = 1;

def write_lcd(byte):
    ser.write( (byte))


def send_command(command):
    hn = command >> 4
    hn = hn & 0x0f
    hn = hn | 0xa0
    write_lcd(chr(hn))
    write_lcd(chr(0xB0)) #RS LOW
    write_lcd(chr(0xC1)) #EN HIGH
    #time.sleep(0.01)
    write_lcd(chr(0xC0)) #EN HIGH
    #time.sleep(0.01)

    hn = command
    hn = hn & 0x0f
    hn = hn | 0xa0
    write_lcd(chr(hn))
    write_lcd(chr(0xB0)) #RS LOW
    write_lcd(chr(0xC1)) #EN HIGH
    #time.sleep(0.01)
    write_lcd(chr(0xC0)) #EN HIGH
    #time.sleep(0.01)

def send_data(data):

    hn = data >> 4
    hn = hn & 0x0f
    hn = hn | 0xa0
    write_lcd(chr(hn))
    write_lcd(chr(0xB1)) #RS LOW
    write_lcd(chr(0xC1)) #EN HIGH
    #time.sleep(0.01)
    write_lcd(chr(0xC0)) #EN low
    #time.sleep(0.01)

    hn = data
    hn = hn & 0x0f
    hn = hn | 0xa0
    write_lcd(chr(hn))
    write_lcd(chr(0xB1)) #RS LOW
    write_lcd(chr(0xC1)) #EN HIGH
    #time.sleep(0.01)
    write_lcd(chr(0xC0)) #EN HIGH
    #time.sleep(0.01)

def lcd_string(string):
    for i in range(len(string)):
        send_data(ord(string[i]))


#initialize the LCD
send_command(0x33)
send_command(0x33)
send_command(0x32)
send_command(0x28)
send_command(0x0e)
send_command(0x01)
send_command(0x6)
send_command(0x80)


cnt = 0;
send_command(0x80) #SET CURSOR TO 0,0
lcd_string("DATA OVER POWER ")

while 1:
	#THIS LOOP CONTINUOUSLY SENT "TESTING %d" on second line
    send_command(0xC0)
    lcd_string("TESTING " + str(cnt))
    time.sleep(.3)
    cnt = cnt + 1
