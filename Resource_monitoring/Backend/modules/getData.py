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
    print(ser.name)
    ser.write(b'hello')
    
    
    #print(data)
    #data = data.replace("n","")
    #data = data.replace("r","")
    #data = data.replace("\\","")
    #ser.write(b'ok')
    #ser.close()
    Start = "Z]"
    list1 = ""
    for i in range(2):
        data = ser.read()
        data = data.decode()
        print(data)
        list1 = str(list1) +str(data)
    if list1 == "Z]":
        for i in range(2):

            data = str(ser.read())
            data = data.replace("b","")
            data = data.replace("'","")
            if data[0] == "\\":
                data = data.replace("\\","")
                data = data.replace("x","")
            else:
                data = format(ord(data), "x")
            print(data)
            list1 = str(list1) +str(data)
            print(list1)
        Data_length = str(list1[4])+(list1[5])
        for i in range(int(Data_length)):
            data = str(ser.read())
            data = data.replace("b","")
            data = data.replace("'","")
            if data[0] == "\\":
                data = data.replace("\\","")
                data = data.replace("x","")
            else:
                data = format(ord(data), "x")
            print(data)
            list1 = str(list1) +str(data)
        Header = list1[2:4]
        print(Header)
        UID =list1[6:10]
        print(UID)
        Status = list1[10:12]
        print(Status)

        print(bytes(Header,'ascii'))

        response1 = "5a5d"+Header+"05"+UID+ "4f4b03"
        print(bytes(response1,'utf-8'))
        response1 = response1.encode()
        ser.write(response1)


