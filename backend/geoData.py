import os
from symbol import parameters
import requests

class IpGeoData:
    def getIpLocation(self,IP):
        IP = IP.strip("\n")
        URL = "https://iplocation.com/"
        header={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        parameters = {"ip":IP}
        r = requests.post(url=URL, params=parameters, headers=header)
        print("[*] geoData for "+str(IP)+":"+str(r.text))
        return r.text
    
    