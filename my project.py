import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.neme_for_number(service_pro,"en"))

from opencage.geocoder import opencagegeocode

key = 'de521b469c804374921ab819533fc569'
geocoder = opencagegeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng],zoom_start= 9)
folium.marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")



