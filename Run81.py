from flask import Flask, render_template, request, redirect, url_for

app1 = Flask(__name__)

@app1.route('/login')
def login():
    return render_template('login.html')

@app1.route('/validate1', methods=['POST'])   #zalidate 這路徑名稱為什麼要和函數名validate 一樣？
def validate():
    if request.method == 'POST' and request.form['email'] == 'test@gmail.com' and request.form['password'] == 'test':
        return redirect(url_for('success'))

    return redirect(url_for('login'))

@app1.route('/success')
def success():
    return 'Logged in successfully.'

if __name__ == '__main__':
    app1.run(debug=True)