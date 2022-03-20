from distutils.log import debug
from flask  import  Flask, flash ,render_template,request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key='xxx'
@app .route('/')
def index9():
     return  render_template('index9.html')

@app.route('/login9',methods =['GET','POST'])
def login9():
    error = None 
    #print error
    if request.method=="POST":
     if request.form['email'] != 'test@gmail.com' or request.form['passwoard'] !='test':
         error = "Invalid accout"
    else:
         flash("login seccessful") 
         return redirect(url_for('index9'))
    return render_template('login9.html', error=error)



if __name__  == '__main__':
     app.run(debug=True)
     
