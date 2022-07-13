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
parkingAvailRem=db.parkingAvailRem



#Loop to monitor continuosly
while 1:
# Read from serial port from arduino
    temp_string = ser.readline().rstrip()

    if temp_string!='': 
        
        temp_value = int(temp_string)
        
        print "Number of cars "
        print(temp_value)
        
        chennaiAvail=parkingAvailRem.find_one({'place':'egmore,chennai'})

    #number of cars less than total capacity
        if( temp_value <= chennaiAvail['total'] ):
            
            print "Updating to cloud"
            
            db.parkingAvailRem.update({
             'place': "egmore,chennai"
                },{
              '$set': {
                'filled': temp_value
                } 
            })

            print "Updated in cloud"
    
        else:
            print "Parking Full"





