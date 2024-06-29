from pymongo import MongoClient
from colorama import Fore, Style 
import os
#from utente import *
        
uri = "mongodb+srv://giorgiociampi:qODlA9DjoW2lpniv@cluster0.zfjgzzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def connection_db():
    global uri
    try:
        db = MongoClient(uri)
        client = db['Test1']
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        
def connection_collection(collection): # concerti e utenti
    global uri
    try:
        client = connection_db()
        collection = client[collection]
        return collection
    except Exception as e:
        print(e)

        
def clear_screen():
    if os.name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")
        
   