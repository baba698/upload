from  flask import Flask, render_template, make_response, session 

app= Flask(__name__)
app.secret_key="test" 
@app.route('/session',methods=['GET'])

def sess():
    res= make_response("<html><body>Session,<a href='/getValue'>Get Value</a></body></html>")
    session['name1']='xijinping'
    return res

@app.route('/getValue')
def getValue():
    if 'name1'  in session:
        name2=session['name1']
        return render_template('getValue.html', name3=name2)
        
 
if __name__ == '__main__':
    app.run(debug=True)       

'''
if __name__=='__mail__':
    app.run(debug=True)
    '''
    
