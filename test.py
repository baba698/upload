from  flask  import  Flask , render_template
app= Flask(__name__)


user = {"username": "xiaoxiao", "bio":"A girl  cho  movies"}
'''
@app.route('/if1')
def if1():
       age=1
       fig =4
       return render_template('if13.html',**locals())

       '''

@app.route('/if1')
def if1():
     goods=[{"name": "apple", "price":32}, {"name":"orange", "price":99}]
     return  render_template('if12.html', **locals())

'''
if __name__ == '__main__':
    app.run(debug=True)

'''

if __name__ == '__main__':
    app.run(debug=True)