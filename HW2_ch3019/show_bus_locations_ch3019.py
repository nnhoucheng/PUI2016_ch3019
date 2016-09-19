from __future__ import print_function
import json
import urllib2 
import os
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_ch3019.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

apikey = sys.argv[1]
bus = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(apikey, bus)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)

bus_len = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print ("Bus Line : " + bus)
print ("Number of Active Buses : %d" %(bus_len))
for i in range(bus_len):
    lo = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    la = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print ("Bus %d is at latitude %f and longitude %f" % (i, la, lo)) 