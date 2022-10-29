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
- [About](#about)
- [Architecture](#architecture-and-design)
- [Design](#design)
- [Demonstration & Features](#demonstration)
- [Technologies Used](#technologies-used)
- [Local Setup & Contributing](#local-setup-and-contribution)
- [License](#license)

### About:

* <a href="https://www.abuseipdb.com/">Abuse IPDB</a>:
AbuseIPDB is a project dedicated to helping combat the spread of hackers, spammers, and abusive activity on the internet.

* <a href="">IPlocation</a>
This free online tool allows you to see the geographical location of any IP address. Just input the IP address and you will be shown the position on a map, coordinates, country, region, city and organization

The objective of this project is to locate abuse IPs from a given list and plot their location on a map by combining the above two to generate KML files which can be imported into Google Maps.

### Architecture and design:

```
*
|_backend
|_frontend

```
### Design:

Backend:

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

* Generation of KML:
We generate the KML using simplekml package of python. The python package simplekml was created to generate kml (or kmz). It was designed to alleviate the burden of having to study KML in order to achieve anything worthwhile with it. If you have a simple understanding of the structure of KML, then simplekml is easy to run with and create usable KML.
<a href="https://pypi.org/project/simplekml/">simplekml</a>

Frontend:

To Be Added

### Demonstration:

Run: 
```
python Main.py
```

Result:
![image](https://user-images.githubusercontent.com/52862591/198849884-4378415d-ec57-45ed-80f9-98b678b725f1.png)

data.json example output file:

![image](https://user-images.githubusercontent.com/52862591/198849913-4103c762-8a8f-48e2-bb37-a8d4628824d4.png)

data.json has the structure:
```
{
    "<IP from the list>": {
        "abuseData": {
            "data": {
            //AbuseIPDB data
            }
        },
        "geoData": {
        //geodata
        }
    },
```
We then feed the data retrieved into JSON files

### Technologies-used
For the backend, I have made use of Python and various libraries

* KML:
KML is a file format used to display geographic data in an Earth browser such as Google Earth. KML uses a tag-based structure with nested elements and attributes and is based on the XML standard. All tags are case-sensitive and must appear exactly as they are listed in the KML <a href="https://developers.google.com/kml/documentation/kml_tut">Reference</a>

### Local Setup and Contribution:
clone the project locally and initialize the .env file. I have provided an example file for the same and install the packages. Once that is done, run the main file of the project or use individual components from the project to suite your needs. Changes and suggestions are always welcome!

### Security:
I take security seriously and so, any security related changes/suggestions are always welcomed!

### Future Scope:
Integrating this with other modules

### License:
<a href="https://github.com/JadenFurtado/geoAbuseIPDB/blob/main/LICENSE.md">The app is under the Creative Commons Zero v1.0 Universal license</a>

