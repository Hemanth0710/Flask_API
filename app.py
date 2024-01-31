from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def name():
    return render_template('index.html')

'''@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)'''


'''@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)'''

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if marks<50:
        res='fail'
    else:
        res='success'
    return render_template('result.html',result=res)

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    
    return redirect(url_for('results',marks=total_score))

if __name__ == '__main__':
    app.run(debug=True)


# flask run (or) python filename
# flask --debug run   (with debug)
