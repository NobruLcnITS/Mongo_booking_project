from pymongo import MongoClient
from geopy.geocoders import Nominatim

connection_string = "mongodb+srv://giorgiociampi:qODlA9DjoW2lpniv@cluster0.zfjgzzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client['Test1']
collection = db["Concerti"]

def get_coordinates(place_name, max_attempts=3):
    geolocator = Nominatim(user_agent="MongoLoca")
    
    for attempt in range(max_attempts):
        try:
            location = geolocator.geocode(place_name)
            if location:
                return location.latitude, location.longitude
            else:
                return [0,0]
        except:
            return [-1,0]



    