from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from flask import jsonify
import json


app = Flask(__name__)
app.secret_key="dev"
app.jinja_env.undefined = StrictUndefined
@app.route('/signout')
def signout():
    session["logged_in_user_id"]=None
    return redirect('/')


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/search_hikes')
def searchform():

    return render_template('search_hikes.html')

# @app.route('/hike_search_result')
# def result():

@app.route('/user_profile')
def profile():
    print('LOGGED IN USER ID:', session['logged_in_user_id'])
    current_logged_in_user = crud.get_user_by_id(session["logged_in_user_id"])
    print( "************** ___ first name =", current_logged_in_user )

    return render_template('user_profile.html',current_logged_in_user=current_logged_in_user)



@app.route('/result_hikes')
def fetch_hikes():
    difficulty=request.args.get("Difficulty")
    pincode= request.args.get("pincode")
    radius=request.args.get("radius")
    tra = crud.get_trail_by_dis_diff(pincode,difficulty,radius)
    print('LOOOOOOOKKKKK HEREEEEEEE', tra)
    return render_template('hike_data.html', trails=tra)
    # return json.dumps([t.as_dict() for t in tra])
    
    # print(tra)
    # return [json.dumps(t.__dict__) for t in tra]
#     print(difficulty)
#     print( radius)
#     print("************")
#     return render_template('result_hikes.html', )
@app.route('/login_users')
def login_user():
    email=request.args.get('email')
    password= request.args.get('password')
    
    #user object
    user = crud.get_user_by_email(email)

   
    # crud file  returns a user and not email or password so to call email and password we use . email or .password
    if user:
        # sessionuser=crud.get_user_by_email(email)
        #loggedin_user
        if password == user.password: 
            # creating a session and putting in primary key as value of session 
            session["logged_in_user_id"]= user.user_id
            print(session)
            return redirect('/user_profile')
        else:
            flash("incorrect password")
            return redirect('/')
    else:
        flash('User does not exist')
        return render_template('signup.html')
       


@app.route('/show_signup')
def show_signup():
    return render_template('signup.html')


@app.route('/detailed_trails')
def detailed_trails():
    trail_id=request.args.get('trail_id')
    detailed_trail=crud.get_trails_by_id(trail_id) # trail id should be same as whose select is selected 
    return render_template('detailed_trails.html',detailed_trail=detailed_trail)

@app.route('/create_users', methods=['POST'])
def register_user():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    email=request.form.get('email')
    password= request.form.get('password')
    
    user= crud.get_user_by_email('email')
    if user:
        print("Cannot create an account with email.Try again")
    else:
        crud.create_user(first_name, last_name,email,password)
        print('Account created! Please login')
 
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)