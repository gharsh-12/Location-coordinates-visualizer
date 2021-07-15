import phonenumbers
import folium
from test import number
key='866ae5c03e454b2f87c66918e0c9b004'
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
yourLocation=geocoder.description_for_number(ch_number,"en")
print(yourLocation)

from phonenumbers import carrier
se_number=phonenumbers.parse(number,"RO")

print(carrier.name_for_number(se_number,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)

query=str(yourLocation)

results=geocoder.geocode(query)
print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
mymap=folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to(mymap)
mymap.save('location.html')