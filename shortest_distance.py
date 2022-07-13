#dependencies
import googlemaps
import pymongo
import operator

import geocoder
g = geocoder.ip('me')
print(g.latlng)

# Requires API key
gmaps = googlemaps.Client(key='AIzaSyBeas6nkC9z-0WSy69rBtkkSlG3T6KAzpg ')


#mongodb connection
#from pymongo import MongoClient
#client = MongoClient()

uri = 'mongodb://renu:mlarsprrrm1998@ds229312.mlab.com:29312/cip'
client = pymongo.MongoClient(uri)


#db access
db = client.cip

#collection access
parkingAvail=db.parkingAvail

#Retrieval of data
chennaiAvail=parkingAvail.find_one({'place':'chennai'})
print(chennaiAvail)

collection = db['parkingAvail']
cursor = collection.find({})

#source
source = "chennai"

distance = {}

for doc in cursor:
        if(doc['available'] > 0):
                print(doc['place'])
                print(doc['available'])
                my_dist = gmaps.distance_matrix(source,doc['place'])['rows'][0]['elements'][0]
                print(my_dist)
                print(my_dist['distance']['value'])
                distance[doc['place']] = my_dist['distance']['value']

print(distance)
sorted_distance = sorted(distance.items(),key=operator.itemgetter(1))
print(sorted_distance)
print("Final Result :")
#print('Place\t--->\t Distance')
for entry in sorted_distance:
        print(str(entry[0]) + ' ----> ' + str(entry[1]))
#isource

#source = "chennai"

#destination
#destination_list = ["coimbatore","salem,india","namakkal"]


# Requires cities name
#for dest in destination_list :
#       print(dest)
#       my_dist = gmaps.distance_matrix(source,doc['place'])['rows'][0]['elements'][0]

# Printing the result
#       print(my_dist)
