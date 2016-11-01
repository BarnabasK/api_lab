from urllib2 import urlopen
from urllib2 import Request
from urlparse import urlparse
import pprint
import json
import sys

def geocode(address_str):
    api_key = 'AIzaSyAfF5CgQO37zohUQI0CgaidJQ65YeYus6I' 
    geocode_url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=true'+ address_str + api_key
    req = Request(geocode_url)
    res = urlopen(req)
    jsonResponse = json.loads(res.read().decode('utf-8'))

    status_code = jsonResponse['status']
    if status_code != 'OK':
        print (status_code)
    else:
        lat = jsonResponse['results'][0]['geometry']['location']['lat']
        lng = jsonResponse['results'][0]['geometry']['location']['lng']
        geo_location= {"Latitude:": lat, "Longitude:": lng}
        print geo_location

geocode("Nakuru")


