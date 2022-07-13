import serial
import time
import datetime
import pymongo
import operator


# Serial Port Configuration for Arduino Board Communication
serial_port          = '/dev/ttyACM1'

# Connect to Serial Port for communication
ser = serial.Serial(serial_port, 9600, timeout=0)


#Connecting to Cloud DB (mlab mongodb)
uri = 'mongodb://renu:mlarsprrrm1998@ds229312.mlab.com:29312/cip'
client = pymongo.MongoClient(uri)


#db access DB Name = cip
db = client.cip

#collection access collection name = parkingAvailRem
slotAvail=db.slotAvail



#Loop to monitor continuosly
while 1:
# Read from serial port from arduino
    temp_string = ser.readline()
    if temp_string!='': 
        print temp_string
        print "length"+str(len(temp_string))
        #temp_value = int(temp_string)
        #if ( temp_value ==0 ):
        #    print "Not Available"
        #else:
        #    print "Available"
        #print "Updating DB"
        #db.slotAvail.update({
        #    'place': "egmore,chennai",
        #    'slotID' : "P1"
        """        },{
              '$set': {
                'status': 0
                }
            })
            
        print "DB Updated"
        """

