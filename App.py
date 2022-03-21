from tokenize import Name
from  flask import  Flask
from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World 喜歡操B</h1>'

from flask import Flask

app = Flask(__name__)
'''
@app.route('/home/<name>')
def index(name):
    return "Welcome to home!{name}"



def index1():
    return ' Hello flask!'


app.add_url_rule('/',"index1" , index1)
 
'''
@app.route('/<name>')

def home(name):
    return render_template('index.html', name=name )



if __name__ == '__main__':
    app.run(debug=True)