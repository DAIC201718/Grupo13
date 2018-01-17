import RPi.GPIO as GPIO
from flask import Flask,request,render_template,redirect, url_for,Response,session, abort
from flask.ext.login import LoginManager, UserMixin,login_required, login_user, logout_user

app = Flask(__name__,template_folder='templates')

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.LOW)


@app.route('/',methods=['GET', 'POST'])
def index():

    return '<h1>Hello World!</h1>'

@app.route('/login',methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']        
        if password == "mikel" and username == "mikel":
            return render_template("template.html")
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
          <div class="container">
             <label><b>Username</b></label>
             <input type="text" placeholder="Enter Username" name="uname" required>
             <label><b>Password</b></label>
             <input type="password" placeholder="Enter Password" name="psw" required>
             <button type="submit">Login</button>
          </div>
        </form>
''')






@app.route('/motor/<action>',methods=['GET', 'POST'])
def action(action):
 if action == "on":
      # Set the pin high:
      GPIO.output(20, GPIO.HIGH)
      # Save the status message to be passed into the template:
      return render_template("template.html",action = action)
 else:
      GPIO.output(20, GPIO.LOW)

      return render_template("template.html",action = action)



if __name__ == "__main__":
    
    app.run(host='0.0.0.0',debug=True)





