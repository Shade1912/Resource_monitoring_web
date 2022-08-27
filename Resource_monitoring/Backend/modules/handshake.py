#number/header/serial/probe/value/date/time/checksum/end - for sending data values
#02/01/0F/03/

#Number/Header/Day/Month/Year/Hours/Mins/cs/end -- clock sync query

#Number/Header/Serial/Probe/repeat query/end -- data loss query
import sys
import glob
import serial

#import serial.tools.list_ports
test_string = "0201"

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    comport = serial_ports()
    comport = str(comport)[1:-1]
    comport = comport.replace("'", "")
    comport = comport.replace('"', "")
    #print(serial.tools.list_ports.comports())
    ser = serial.Serial(comport)
    #print(ser.name)
    data = ser.write()