import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
import requests

os.system('dropdb trails')
os.system('createdb trails')

model.connect_to_db(server.app)
model.db.create_all()

API_KEY = os.environ['API_KEY']
# getting  data from api based on lat and log and distance as params (san francisco right now hard coded which will be changed later ) 

res= requests.get(f'https://www.hikingproject.com/data/get-trails?lat=37.7739&lon=-122.4312&maxDistance=10000&maxResults=500&key={API_KEY}' ) 
hike_search_results= res.json()


# print(search_results)

list_of_hiking_dicts= hike_search_results['trails']
#print(list_of_hiking_dicts)

trails_in_db=[]
for hike in list_of_hiking_dicts:
#     print(hike)

    trail_api_id=hike.get('id')
    trail_name=hike.get('name')
    latitude=hike.get('latitude')
    longitude=hike.get('longitude')
    summary=hike.get('summary')
    image=hike.get('imgSqSmall')
    difficulty=hike.get('difficulty')
    star_rating=hike.get('star')
    trail_length=hike.get('length')
    comments='no comments'

    db_trails=crud.create_trail(trail_api_id,trail_name,latitude,longitude,summary,image,difficulty,star_rating,trail_length,comments)
    trails_in_db.append(db_trails)


    print(trails_in_db)


# create a hike to add to data base create instances of classes defined in model.py and add it to my database
#db.session.add()