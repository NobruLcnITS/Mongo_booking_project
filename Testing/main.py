from pymongo import MongoClient
import os
from colorama import Fore, Style 
import time
from get_coordinates import get_coordinates
from filtercreators import *
from datetime import datetime, date
import re
import hashlib
from connectiondb import connection_collection, clear_screen
from selctor import *
from session import *

users_collection = connection_collection('utenti')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def mongo_exists(username):
    global users_collection 
    return users_collection.count_documents({"username": username}) > 0

def add_user(username, password):
    global users_collection
    if mongo_exists(username):
        return None 
    user = {
        "username": username,
        "password": password,
        "tickets": []
    }
    return users_collection.insert_one(user)

def sign_up():
    global users_collection
    user = str(input('Inserisci il tuo nome: ').strip())
    check= mongo_exists(user) # .find per cercare l'utente sul database
    if check==False and user!=' ':
        while True:
            password = input('Inserisci la password: ').strip()
            if password!= '':
                if password.upper() != 'ESC':
                    password_valid = input('Conferma la password: ').strip()
                    if password_valid.upper() != 'ESC':
                        if (password != password_valid):
                            print('Le due password sono diverse') 
                        else:
                            clear_screen()
                            print('Utente Registrato correttamente')
                            add_user(user, hash_password(password))
                            break
                    else:
                        clear_screen()
                        break
                else:
                    clear_screen()
                    break
            else:
                clear_screen()
                print('Hai inserito una password vuota')
    else:
        clear_screen()
        print(f"L'utente {user} è già registrato")
        
def login(): 
    
    user = str(input('Inserisci il tuo nome utente: ').strip())
    password = input('Inserisci la password: ').strip()

    check= mongo_exists(user)
    print(check)
    if check==True:
        password_encripted = users_collection.find_one({"username": user}).get('password')
        
        if hash_password(password)==password_encripted:
            clear_screen()
            print(f"{user} hai effettuato correttamente il login")
            return user
        else:
            clear_screen()
            print('Dati non inseriti correttamente')
            return None
    else:
        clear_screen()
        print('Dati non inseriti correttamente')
        return None