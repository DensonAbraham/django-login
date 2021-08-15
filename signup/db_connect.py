from django.http.request import QueryDict
import pymongo
from pymongo import collection
from pymongo.mongo_client import MongoClient  

def conn():
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['admin'] 
    collection = db['signups']



def insert(data_received): 
    conn()
    data = data_received
    print(data) 
    email_id = data_received["email"]  
    user = data_received["username"] 
    print(email_id) 
    email_check = collection.find_one({'email':email_id})  
    user_check = collection.find_one({'username':user})
    if email_check == None or user_check == None:
        collection.insert_one(data)    
        return True 
    else: 
        return False
    

def verify(creds):  
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['admin'] 
    collection = db['signups']
    user = creds["username"]
    password = creds["pass"] 
    verification = collection.find_one({"username":user, "pass":password})
    if verification == None: 
        return False
    else: 
        return True 

