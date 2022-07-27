from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "ellahazan3108"
password = "ellahazan"
facebook_friends=["Lia","Tal","Roni", "Maya", "Abigail", "Yasmena", "Shay", "Lotem"]

for friend in facebook_friends:
  print(friend)




@app.route('/',methods = ['GET','POST'])  # '/' for the default page
def login(): 
    error = None
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('home'))    

  
@app.route('/home')  # '/' for the default page
def home():
     return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:myfriend>',methods = ['GET','POST']) 
def friend_exists(myfriend):
    return "welcome to profile page %s" % myfriend 
    return render_template('friend_exists.html', friend=myfriend, facebook_friends=facebook_friends)    
# '/' for the default page

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)