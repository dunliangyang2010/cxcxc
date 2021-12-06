from flask import Flask, render_template, url_for, redirect, request
import json
from flask import session
app = Flask(__name__) # initialize

users=[{"name": "Andy", "age":"25", "height": "183", "weight":"80"},
	   {"name": "Bob",  "age":"32", "height": "176", "weight":"70"},
       {"name": "Candy","age":"24", "height": "160", "weight":"45"},
]

@app.route('/')
def main():
    return render_template('main.html') 

@app.route('/user')
def user():
    return render_template('user.html', users=users) 

if __name__=="__main__":
    app.run(debug=True)