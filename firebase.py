import firebase_admin
from firebase_admin import credentials, db
import time
cred = credentials.Certificate(
    "plant-ai-bot-skynet-phase-3-firebase-adminsdk-v3gva-ab64fb032e.json")
firebase_admin.initialize_app(
    cred, {'databaseURL': "https://plant-ai-bot-skynet-phase-3-default-rtdb.firebaseio.com/"})
ref = db.reference("/")
f = open("C:/Users/krish/Documents/Plant AI bot continuous data.csv")
lines = f.readlines()
for i in range(0, len(lines), 6):
	dta={"Data":{ "Soil Moisture": (lines[i].split(',')[1]),
            "Light Sensor": (lines[i+1].split(',')[1]),
            "Humidity level": (lines[i+2].split(',')[1]),
            "Temperature in C": (lines[i+3].split(',')[1].replace('*C',"")),
            "Temperature in F": (lines[i+4].split(',')[1].replace('*F',"").replace("\"",'')),
            "Head Index": (lines[i+5].split(',')[1].replace('*F',""))}}
	ref.set(dta)
	time.sleep(3)
    
	