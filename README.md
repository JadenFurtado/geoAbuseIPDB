# geo Abuse IP DB

```
                           _                    _____ _____  _____  ____  
                     /\   | |                  |_   _|  __ \|  __ \|  _ \ 
   __ _  ___  ___   /  \  | |__  _   _ ___  ___  | | | |__) | |  | | |_) |
  / _` |/ _ \/ _ \ / /\ \ | '_ \| | | / __|/ _ \ | | |  ___/| |  | |  _ < 
 | (_| |  __/ (_) / ____ \| |_) | |_| \__ \  __/_| |_| |    | |__| | |_) |
  \__, |\___|\___/_/    \_\_.__/ \__,_|___/\___|_____|_|    |_____/|____/ 
   __/ |                                                                  
  |___/                                                                       

```
A wrapper around abuse IPDB for analyzing IPs as per their geo locations.

## Table of contents:
- [About](#About)
- [Architecture](#architecture-and-design)
- [Design](#design)
- [Demonstration & Features](#demonstration)
- [Technologies Used](#technologies-used)
- [Local Setup & Contributing](#contributing)
- [License](#license)

### About:

* <a href="https://www.abuseipdb.com/">Abuse IPDB</a>:
AbuseIPDB is a project dedicated to helping combat the spread of hackers, spammers, and abusive activity on the internet.

* <a href="">IPlocation</a>
This free online tool allows you to see the geographical location of any IP address. Just input the IP address and you will be shown the position on a map, coordinates, country, region, city and organization

The objective of this project is to locate abuse IPs from a given list and plot their location on a map by combining the above two to generate KML files which can be imported into Google Maps.

### architecture and design:

```
*
|_backend
|_frontend

```
### Design:

* Getting the data from Abuse IPDB:
```
curl -G https://api.abuseipdb.com/api/v2/check \
  --data-urlencode "ipAddress=118.25.6.39" \
  -d maxAgeInDays=90 \
  -d verbose \
  -H "Key: YOUR_OWN_API_KEY" \
  -H "Accept: application/json"
```
* Getting the data from IPlocation:

```
curl https://api.iplocation.net/?ip=8.8.8.8

```

We then feed the data retrieved into JSON files

### Demonstration:
Run: 
```
python Main.py
```

### Technologies-used
For the backend, I have made use of Python and various libraries

* KML:
KML is a file format used to display geographic data in an Earth browser such as Google Earth. KML uses a tag-based structure with nested elements and attributes and is based on the XML standard. All tags are case-sensitive and must appear exactly as they are listed in the KML <a href="https://developers.google.com/kml/documentation/kml_tut">Reference</a>

### Local Setup and Contribution:

### Security:
I take security seriously and so, any security related changes/suggestions are always welcomed!

### Future Scope:
Integrating this with other modules

### License:
<a href="https://github.com/JadenFurtado/geoAbuseIPDB/blob/main/LICENSE.md">The app is under the Creative Commons Zero v1.0 Universal license</a>

