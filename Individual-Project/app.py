from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session 
#import stmplib
#signup/in
import pyrebase
Config = {
  "apiKey": "AIzaSyAxi64BOVf7_Fd16PKs3Zpxwuf7HOoHjNg",
  "authDomain": "my-project-a4954.firebaseapp.com",
  "projectId": "my-project-a4954",
  "storageBucket": "my-project-a4954.appspot.com",
  "messagingSenderId": "259680062889",
  "appId": "1:259680062889:web:ff06e932dbea0c8fc1c8b8",
  "measurementId": "G-Y564FVJ058",
  "databaseURL": " https://my-project-a4954-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db=firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
     error = ""
     if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        login_session['user'] = auth.sign_in_with_email_and_password(email,password)
        return redirect(url_for('htmlcss'))
        
            
            
     else:
        return render_template("signin.html")  

@app.route('/lion', methods=['GET','POST'])
def box1():
    return render_template("lion.html")

@app.route('/cat', methods=['GET','POST'])
def box2():
    return render_template("cat.html")

@app.route('/dis', methods=['GET','POST'])
def box3():
    return render_template("dis.html")

@app.route('/htmlcss')
def htmlcss():
	return render_template("htmlcss.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('htmlcss'))
        
            
    return render_template("signup.html")

@app.route('/htmlcss', methods=['GET', 'POST'])
def articles():
    if request.method == 'POST':
        article = {"Email": request.form['Email'], "Subject": request.form['Subject'], "Comment": request.form['Comment']}
        db.child("htmlcss").push(article)
        return render_template("htmlcss.html")
    return render_template("htmlcss.html")

@app.route('/contacts')
def contacts():
    contacts = db.child("htmlcss").get().val()
    return render_template('contacts.html' , contacts=contacts)

    

"""@app.route('/htmlcss', methods=['GET', 'POST'])
def htmlcss():
    error =""
    if request.method== 'POST':
        
        post = {"uid": login_session['user']['localId'],"title":request.form['title'], "text":request.form['text']}
        db.child("Offers").push(Post)
        return redirect(url_for('add post'))
        
            
    return render_template("htmlcss.html")"""
    


"""@app.route('/htmlcss', methods=['GET', 'POST'])
def add_tweet():
    return render_template("htmlcss.html")

    @app.route('/lion', methods=['GET', 'POST'])
def lion():
    return render_template("lion.html")"""

"""server = stmplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("ahmadqawasmi06@gmail.com", "PASSWORD")
server.sendmail("ahmadqawasmi06@gmail.com", email,message)"""

if __name__ == '__main__':
    app.run(debug=True)
#contact us

         