from flask import  Flask,render_template 
from flask  import redirect
from  flask  import  abort 

'''from  flask.ext.script import Manager '''
app = Flask(__name__)
'''
@app.route('/')
def index():
    return '<h1> Hello World!</h1>'   

return redirect('http://www.google.com')   '''


'''
@app.route('/user/<id>')
def  get_user(id):
    user =load_user(id)
    if not user:
        abort(404)
    return  '<h1> Hello, %s </h1>'  % user.name
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%S!</h1>' %name
if __name__=='__main__':
        app.run(debug=True)   '''
        


@app.route('/<name>')
def  home(name):
    return render_template('index.html',name=name)


if  __name__=='__mail__':
       app.run(debug=True)
