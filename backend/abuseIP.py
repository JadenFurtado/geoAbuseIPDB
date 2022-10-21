import os
from symbol import parameters
import requests
from dotenv import load_dotenv

class AbuseIPDB:
    def __init__(self) -> None:
        load_dotenv()

    def getABIPResults(self,IP):
        IP = IP.strip("\n")        
        API_KEY = os.getenv('ABUSE_IP_API_KEY')
        URL = "https://api.abuseipdb.com/api/v2/check?ipAddress="+IP+"&maxAgeInDays=150"
        header={
            "Key": API_KEY,
            "Accept": "application/json"
        }
        r = requests.get(url = URL, params = parameters,headers=header)
        print(r.text)
        return r.text
    