from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class USER(db.Model):
    """user data"""
    __tablename__="users"

    user_id= db.Column (db.Integer, primary_key= True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)
    home_zipcode= db.Column(db.Integer)

    def __repr__(self):
        return f'<USER user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email} password={self.password} >'

class TRAIL(db.Model):
    """hike trails data which is fetched from API"""
    __tablename__= "trails"

    trail_id = db.Column(db.Integer, primary_key=True)
    trail_api_id = db.Column(db.Integer)
    trail_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    summary = db.Column(db.String)
    image = db.Column(db.String)
    difficulty = db.Column(db.String)
    star_rating = db.Column(db.Float)
    trail_length = db.Column(db.Float)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<TRAIL trail_id{self.trail_id} >'
  
class USERS_SELECTED_TRAIL(db.Model):
    """hike trails data which is fetched from API"""
    __tablename__= "user_selected_trails"

    user_selected_trails_id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'))
    trail_id=db.Column(db.Integer,db.ForeignKey('trails.trail_id'))
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
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
