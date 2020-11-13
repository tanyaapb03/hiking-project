from model import db, USER, TRAIL, USERS_SELECTED_TRAIL, connect_to_db
import server
#import requests
import pgeocode




def create_user(email,password):
    user = USER(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user
def create_trail(trail_api_id,trail_name,latitude,longitude,summary,image,difficulty,star_rating,trail_length):
    
    trail =TRAIL( 
    trail_api_id=trail_api_id,
    trail_name=trail_name,
    latitude=latitude,
    longitude=longitude,
    summary=summary,
    image=image,
    difficulty=difficulty,
    star_rating=star_rating,
    trail_length=trail_length)

    db.session.add(trail)
    db.session.commit()

    return trail

def get_trails():
# get all trails
    return TRAIL.query.all()

def get_trail_by_dis_diff(pincode,difficulty,radius):
    radius=float(radius)
    longi,lat = get_latlong_from_pincode(pincode)
    return TRAIL.query.filter(TRAIL.difficulty==difficulty).filter(TRAIL.latitude.between(lat - radius, lat + radius)).filter(TRAIL.longitude.between(longi- radius, longi + radius)).limit(10).all()
    
def get_data_by_parameter(difficulty):
    
    return TRAIL.query.filter(TRAIL.difficulty==difficulty).all()

# def get_data_by_radius(radius):
    
#     return TRAIL.query.filter(TRAIL.radius==radius).all()

# def create_user_selected_trails(user_selected_trail_id,user_id,trail_id):
#     selection=USERS_SELECTED_TRAIL(
#         user_selected_trail_id=user_selected_trail_id,
#         user_id=USER.user_id,
#         trail_id=TRAIL.trail_id)

#     db.session.add(selection)
#     db.session.commit()

#     return selection

    

def get_latlong_from_pincode(pincode):
    
    nomi = pgeocode.Nominatim('us')
    result=nomi.query_postal_code(pincode)
    print(result)
    longi=result.longitude
    lat=result.latitude
    print (longi)
    print(lat)


    return (longi,lat)


def get_user_by_email(email):
    return USER.query.filter(USER.email==email).first()

def get_user_by_id(id):

    return USER.query.get(id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)