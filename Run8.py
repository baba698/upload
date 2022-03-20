
from flask import  Flask,render_template,request,redirect,url_for
 
 
app1 =Flask(__name__)
@app1.route('/login81')
def login81():
     return render_template('login81.html')


@app1.route('/validate', methods=['POST'])

def validate():
    if request.method== 'POST' and request.form['email'] =='test@gmail.com' and request.form['password']=='test':
        return redirect(url_for(success8))
    return redirect(url_for(login81))

@app1.route('/success8')

def success8():
    return 'logged in successfully'


'''
if __name__=='__mail__':
    app1.run(debug=True)
    '''
if __name__ == '__main__':
    app1.run(debug=True)


