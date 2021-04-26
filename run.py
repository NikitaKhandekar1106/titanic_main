from flask import Flask,jsonify,render_template,request
import functions,test_model,titanic_main,titanic_db
import pickle

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        data=request.form
        response=titanic_db.register(data)
    return jsonify({'msg':response})

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        data=request.form
        response=titanic_db.login(data)
    return jsonify({'msg':response}) 

@app.route('/survived_prediction',methods=['GET','POST'])
def survived_prediction():
    if request.method=='POST':
        data=request.form
        age=int(data['age'])
        pclass=int(data['pclass'])
        male=int(data['male'])
        print('age,pclass,male',age,pclass,male)
        prediction=test_model.get_survived_predict( age,pclass, male)
        titanic_db.survived(age, pclass, male, prediction)
        return('passenger status:{}'.format(prediction))
    return render_template('home.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001)