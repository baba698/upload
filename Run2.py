from  flask import  Flask, make_response
app  = Flask(__name__)
@app.route('/cookie', methods=['GET'])
def cookie():
    res =make_response("<html><body> cookie</body></html>")
    res.set_cookie('name','xijinping')
    return res

if __name__=='__main__':
    app.run(debug=True)
