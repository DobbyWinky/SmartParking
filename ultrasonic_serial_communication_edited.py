import serial
import time
import datetime
import pymongo
import operator


# Serial Port Configuration for Arduino Board Communication
serial_port          = '/dev/ttyACM0'

# Connect to Serial Port for communication
ser = serial.Serial(serial_port, 9600, timeout=0)


#Connecting to Cloud DB (mlab mongodb)
uri = 'mongodb://renu:mlarsprrrm1998@ds229312.mlab.com:29312/cip'
client = pymongo.MongoClient(uri)


#db access DB Name = cip
db = client.cip

#collection access collection name = parkingAvailRem
slotAvail=db.slotAvail


line=[]
line+='\r'
line+='\n'
#Loop to monitor continuosly
while 1:
# Read from serial port from arduino
    temp_string = ser.read()
    if temp_string=='&':
        slotId=line[2]
        statusVal=line[4]
        if statusVal=='0':
            status="Available"
        if statusVal=='1':
            status="Not Available"
        print "SlotId="+slotId+":Status="+status
        print "Updating DB"
        db.slotAvail.update({
            'place': "egmore,chennai",
            'slotID' : slotId
                },{
              '$set': {
                'status': status
                }
            })

        print "DB Updated"
        line=[]
    else:
        line+=temp_string

