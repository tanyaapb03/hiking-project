from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class USER(db.Model):
    """user data"""
    __tablename__="users"

    user_id= db.Column (db.integer,primary_key= True, auto_increment= True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.string)
    email=db.Column(db.String)
    Password=db.Column(db.String)
    home_zipcode= db.Column(db.Integer)

    def __repr__(self):
        return f'<USER user_id={self.user_id} email={self.email} home_zipcode{self.home_zzipcode} >'

class TRAIL(db.Model):
    """hike trails data which is fetched from API"""
    __tablename__= "tails"

    trail_id=db.Column(db.Integer,primary_key=True,auto_increment=True)
    trail_api_id=db.Column(db.Integer)
    trail_name=db.Column(db.string)
    latitude=db.Column(db.integer)
    longitude=db.Column(db.integer)
    summary= db.Column(db.varchar)
    image=db.Column(db.image)
    difficulty=db.Column(db.integer)
    star_rating=db.Column(db.float)
    trail_length=db.Column(db.float)


    def __repr__(self):
        return f'<TRAIL trail_id{self.trail_id} >'
  
class USERS_SELECTED_TRAIL(db.Model):
    """hike trails data which is fetched from API"""
    __tablename__= "user_selected_trails"

    user_selected_trails_id=db.Column(db.Integer,primary_key=True,auto_increment=True)
    user_id=db.Column(db.Integer)
    trail_id=db.Column(db.Integer) 
    def __repr__(self):
        return f'<USERS_SELECTED_TRAIL{self.user_selected_trails}>'

def connect_to_db(flask_app, db_uri='postgresql:///trails', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
