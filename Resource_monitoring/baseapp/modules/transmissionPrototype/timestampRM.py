import datetime

def getTimestamp():
    return str(datetime.datetime.now())

def getTimestampForEncodedString(split_string):
    return str(split_string+str(datetime.datetime.now()))