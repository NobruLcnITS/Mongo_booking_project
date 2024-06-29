from datetime import datetime

def concert_name_checker(concert):
    if isinstance(concert, str):
        return {
        "nome": {"$regex": concert, "$options": "i"}  
        }
    elif isinstance(concert, list):
        return {
            "$or": [{"nome": {"$regex": c, "$options": "i"}} for c in concert]
        }
        


def geo_checker(lon, lat, maxdistance):
    return {
        "luogo.posizione": {
            "$geoWithin": {
                "$centerSphere": [[lon, lat], maxdistance / 6371000]
            }
        }
    }
    
def artist_checker(artist):
    if isinstance(artist, str):
        return {
            "artista": {"$regex": artist, "$options": "i"}
        }
    elif isinstance(artist, list):
        return {
            "$or": [{"artista": {"$regex": a, "$options": "i"}} for a in artist]
        }
        
def genre_checker(genre):
    if isinstance(genre, str):
        return {
            "genere": {"$regex": genre, "$options": "i"}
        }
    elif isinstance(genre, list):
        return {
            "$or": [{"genere": {"$regex": g, "$options": "i"}} for g in genre]
        }
                       
def available_tickets_checker():
    return {
        "$expr": {
            "$gt": [{"$sum": "$biglietti_disponibili"}, 0]
        }
    }

def price_checker(max_price):
    return {
        "prezzo_biglietti": {
            "$elemMatch": {
                "$lte": max_price
            }
        }
    }
    
def date_checker(start_date=None, end_date=None):
    date_filter = {}
    
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        date_filter["$gte"] = start_date
    
    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        date_filter["$lte"] = end_date
    
    return {"data": date_filter} if date_filter else {}

def validazione_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False