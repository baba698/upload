from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "xxx"

@app.route('/')
def index9():
    return render_template('index91.html')

@app.route('/login91', methods=['GET', 'POST'])
def login91():
    error = None
    if request.method == "POST":
        if request.form['email'] != 'test@gmail.com' or request.form['password'] != 'test':
            error = "Invalid account"
        else:
            flash("Login successfully")
            return redirect(url_for('index9'))

    return render_template('login91.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)