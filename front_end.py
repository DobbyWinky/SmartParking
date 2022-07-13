import googlemaps
import pymongo
import operator

from flask import Flask
app = Flask(__name__)


uri = 'mongodb://renu:mlarsprrrm1998@ds229312.mlab.com:29312/cip'
client = pymongo.MongoClient(uri)

#db access
db = client.cip


@app.route('/')
def shortest_parking():
	output = "List based on distance from current point : "
	gmaps = googlemaps.Client(key='AIzaSyBeas6nkC9z-0WSy69rBtkkSlG3T6KAzpg ')
	
	#collection access
	parkingAvail=db.parkingAvail
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

	output += "<table border = 1>";
	
	for entry in sorted_distance:
	        print(str(entry[0]) + ' ----> ' + str(entry[1]))
	        output += "\n<tr><td><a href=" + str(entry[0]) + ">" + str(entry[0]) + "</a></td><td>" + str(entry[1]) + "</td></tr>"
	
	output += "</table>";

	return output

@app.route('/<place>')
def slot(place):
	collection = db['slotAvail']
	cursor = collection.find({})

	output1 = "Slot Table<br><table border = 1>";

	for doc in cursor:
		print (doc['slotID'])
		if(doc['status'] == 1):
			output1 += "<tr><td>"+doc['slotID']+"</td><td>"+"Availbale"+"</td></tr>";
		else:
			output1 += "<tr><td>"+doc['slotID']+"</td><td>"+"Not Availbale"+"</td></tr>";

	return output1

if __name__ == '__main__':
	app.run()