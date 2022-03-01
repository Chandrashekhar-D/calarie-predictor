import flask
from flask import Flask, render_template, request

import pandas as pd 

import pickle

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

def ValuePredictor(data):
    loaded_model =pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(data)
    return result

@app.route("/result", methods=["POST"])
def result():
    predict_dict = request.form.to_dict()
    for i in predict_dict.keys():
        if(i=="Gender"):
            predict_dict[i] = int(predict_dict[i])
            predict_dict[i]=[predict_dict[i]]
        else:
            predict_dict[i] = float(predict_dict[i])
            predict_dict[i]=[predict_dict[i]]
    predict_df = pd.DataFrame.from_dict(predict_dict)
    print(predict_df)
    result = ValuePredictor(predict_df)
    print(result)
    print(predict_df)
    result = ValuePredictor(predict_df)
    return render_template("result.html",prediction=result)


if(__name__)==("__main__"):
    app.run(debug=True)