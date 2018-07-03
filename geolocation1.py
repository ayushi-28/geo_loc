import requests
import googlemaps

gmaps = googlemaps.Client(key='###########')
loc = gmaps.geolocate()
print(loc)