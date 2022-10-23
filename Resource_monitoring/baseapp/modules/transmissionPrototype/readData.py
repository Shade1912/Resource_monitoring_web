def readData(ser):
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
        else:
            list1=""
    return list1