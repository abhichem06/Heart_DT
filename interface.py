from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import Heart
app = Flask(__name__)

########################################################################

@app.route('/') 
def hello_flask():
    return 'Hello Mock Group_06'

#########################################################################


@app.route('/predict')
def get_predicted():

    data = request.get_json()
    age = eval(data['age'])
    sex = eval(data['sex'])
    cp = eval(data['cp'])
    trestbps = eval(data['trestbps'])
    chol = eval(data['chol'])
    fbs = eval(data['fbs'])
    restecg = eval(data['restecg'])
    thalach = eval(data['thalach'])
    exang = eval(data['exang'])
    oldpeak = eval(data['oldpeak'])
    slope = eval(data['slope'])
    ca = eval(data['ca'])
    thal = eval(data['thal'])
    
    HD = Heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result=HD.get_predicted()
    
    
    
    
    return jsonify({"Result":f"Predicted  Patient Having Heart Disease : {result}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)