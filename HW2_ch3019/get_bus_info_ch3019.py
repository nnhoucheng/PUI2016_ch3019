from __future__ import print_function
import json
import urllib2 
import os
import sys

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info_ch3019.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

apikey = sys.argv[1]
bus = sys.argv[2]
fout = open(sys.argv[3], "w")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"\
%(apikey, bus)

response = urllib2.urlopen(url)
d = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(d)

data = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_len = len(data)

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(bus_len):
    lo = data[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    la = data[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    if data[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
        sn = 'N/A'
        ss = 'N/A'
    else:
        sn = data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        ss = data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]\
        ['Extensions']['Distances']['PresentableDistance']
    fout.write("%f,%f,%s,%s\n" % (la, lo, sn, ss))
    
fout.close()
