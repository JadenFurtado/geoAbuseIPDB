import simplekml
import json
  
# Opening JSON file
f = open('fileloc.json')
# Add a marker
  
# returns JSON object as 
# a dictionary
data = json.load(f)

a = open('file.json')
# Add a marker
  
# returns JSON object as 
# a dictionary
abuseIP = json.load(a)

k=0
# Iterating through the json
# list
# save KML to a file

kml = simplekml.Kml()
for entry in data['locations']:
    kml.newpoint(name=str(abuseIP['file'][k]['data']['ipAddress']),description="usage: "+str(abuseIP['Payemt.php'][k]['data']["usageType"])+",\nisp:"+abuseIP['Payemt.php'][k]['data']["isp"]+",\ndomain:"+str(abuseIP['Payemt.php'][k]['data']["domain"])+",\nreports "+str(abuseIP['Payemt.php'][k]['data']["totalReports"]),coords=[(entry['lng'],entry['lat'])])  # lon, lat, optional height
    kml.save("file.kml")
    k+=1