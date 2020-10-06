import requests
import json
import tkinter as tk
from pprint import pprint


#Get Key
#This is a file not in my respository I don't want you to have it
file = open("/Users/emanuel.paduret/Documents/SL:HL Computer Science/TERM 1/Git_Hub_Repo_EPaduret/DP_CS_Code_EPaduret/API_Keys/fixerkey.txt","r")

#read is an instance method for file object
key = file.read()


#get is a static/class method in the request module
resp = requests.get('http://data.fixer.io/api/latest?access_key=821ce31422657d4a6dc4c593e8e353bc')
#resp = requests.get('https://jsonplaceholder.typicode.com/comments')


#Converts response to JSON - a dictionary
data = resp.json()

pprint(data["base"])
pprint(data["date"])
pprint(data["rates"]["CAD"])
pprint(data["rates"]["GBP"])
#pprint(data["rates"])
