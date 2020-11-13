from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from flask import jsonify
import json

app = Flask(__name__)
app.secret_key="dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/search_hikes')
def searchform():

    return render_template('search_hikes.html')

# @app.route('/hike_search_result')
# def result():


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
    email=request.form.get('email')
    password= request.form.get('password')
    if email==crud.get_user_by_email('email'):
        return redirect('/search_hikes')
    else:
        flash('User does not exist')
        return render_template('signup.html')



@app.route('/create_users', methods=['POST'])
def register_user():
    email=request.form.get('email')
    password= request.form.get('password')
    user= crud.get_user_by_email('email')
    if user:
        print("cannot create an account with email.Try again")
    else:
        crud.create_user(email,password)
        print('account created ! please login in')
 
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)