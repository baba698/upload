

from msilib.schema import _Validation_records
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, PasswordField
from  wtforms.validators import DataRequired, EqualTo, Length,Email

app = Flask(__name__)

app.secret_key="xxx"

class RegisterForm(FlaskForm):
      username1=StringField(label="username:",  validators = [DataRequired()])
      email1= StringField(label="email:", validators=[DataRequired(), Email(message='email format error')] )
      password1= PasswordField(label="password:", validators =[DataRequired(), Length(6,16, message='password format error')])
      password2=PasswordField(label='comfirm password:', validators= [DataRequired(), Length(6,16,message='password format error'), EqualTo('password1', message=' password not mathch')])
      submit1=SubmitField(label="Register:")



@app.route('/10',methods=['GET', 'POST'])
def login10():
      Register_form1= RegisterForm()
     
      if Register_form1.validate_on_submit():
           username1=request.form.get('username1')
           email1=request.form.get('email1')
           password= request.form.get('password')
           password2=request.form.get('password2')
           if  username1 == 'wang' and  password==password2 and  email1 =='test@gmail.com':
                return 'Register success, username:{}, email:{}, password:{}' .format(username1,email1, password)
           else:
               return  'error5666'
      else:
        return 'Invalid58888'
        
        return  render_template('Register10.html', form=RegisterForm)

if __name__ == '__main__' :
       app.run(debug=True)





    



