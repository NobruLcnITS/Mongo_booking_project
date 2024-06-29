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