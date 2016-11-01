import urllib
import urllib.parse
import urllib.request
import pprint
import json
import sys

def geocode(address_str):
    address = urllib.parse.quote(address_str)
    geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % address
    req = urllib.request.urlopen(geocode_url)
    jsonResponse = json.loads(req.read().decode('utf-8'))

    status_code = jsonResponse['status']
    if status_code != 'OK':
        print (status_code)
    else:
        lat = jsonResponse['results'][0]['geometry']['location']['lat']
        lng = jsonResponse['results'][0]['geometry']['location']['lng']
        geo_location= {"Latitude:": lat, "Longitude:": lng}
    return geo_location