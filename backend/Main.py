from dotenv import load_dotenv
from abuseIP import AbuseIPDB
import os
from dotenv import load_dotenv
from geoData import IpGeoData
import json

if __name__=="__main__":
    print("[*] Starting geoAbuseIPDB:")
    load_dotenv()
    pathToIPsFile = os.getenv("IP_TEXT_FILE")
    abuseip = AbuseIPDB()
    geoip = IpGeoData()
    abuseData = dict()
    with open(pathToIPsFile, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            print(line)
            abuseData[line]=dict()
            aipData = abuseip.getABIPResults(line)
            abuseData[line]['abuseData'] = json.loads(str(aipData))
            gipData = geoip.getIpLocation(line)
            abuseData[line]['geoData'] = json.loads(str(gipData))
    print(abuseData)
    with open(os.getenv("OUTPUT_FILE"), 'w') as fp:
        json.dump(abuseData, fp)
