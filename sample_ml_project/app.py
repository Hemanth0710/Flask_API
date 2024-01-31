from flask import Flask,render_template,request
from sklearn.ensemble import RandomForestClassifier
import pickle

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Pclass=int(request.form['Pclass'])
        Sex=int(request.form['Sex'])
        Age=float(request.form['Age'])
        SibSp=int(request.form['SibSp'])
        Parch=int(request.form['Parch'])
        Fare=float(request.form['Fare'])
        Embarked=float(request.form['Embarked'])

        data=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]]

        tit_rf=pickle.load(open('tit_rf.pkl','rb'))
        pred=tit_rf.predict(data)[0]
        
    return render_template('predict.html',prediction=pred)



if __name__=='__main__':
    app.run(debug=True)