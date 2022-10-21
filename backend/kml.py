import simplekml
import json
  
class KML:
    def generateKML(self,filePath,kmlFilePath):
        f = open(filePath)
        data = json.load(f)
        kml = simplekml.Kml()
        for entry in data:
            print("[*] Adding "+entry+" to KML")
            kml.newpoint(name=str(entry),description="usage: "+str(data[entry]['abuseData']['data']['usageType'])+",\nisp:"+data[entry]['abuseData']['data']['isp']+",\ndomain:"+str(data[entry]['abuseData']['data']['domain'])+",\nreports "+str(data[entry]['abuseData']['data']['totalReports']),coords=[(data[entry]['geoData']['lng'],data[entry]['geoData']['lat'])])  # lon, lat, optional height
            kml.save(kmlFilePath)
