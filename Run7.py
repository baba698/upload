from  flask  import  Flask,render_template,request
app=Flask(__name__)
@app.route('/index7')
def index7():
    return render_template('index7.html')


@app.route('/success7', methods=['POST'])
def success():
    if request.method =='POST':

     f= request.files['file']
     f.save(f.filename)
     return render_template('success7.html', name=f.filename)
     



if __name__ == '__main__':
    app.run(debug=True)
