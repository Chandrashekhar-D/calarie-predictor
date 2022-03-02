# calarie-predictor
app.py is flask application
create virtual environment if you're making changes in model

ml-model folder has model created for xgboost add following lines at the end of code to get pickle file

import pickle
pickle.dump(model,open("model.pkl ", "wb"))

1. Create venv
  python3 -m venv venv
	Activate venv
	./Scripts/activate

2. Install required libraries
  pip install <name>
  
	flask
	pandas
	scikit-learn
	gunicorn
3. pip3 freeze > requirements.txt

4. creat flask app
  flask run
  to run flask app in development mode use following command --
	export FLASK_ENV=development(in bash)
5. install templates
7. convert dict to pd df

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

6. deploy ml with pickle
  pickle.load(open("model.pkl", "rb"))
7. create procfile
  echo "web: gunicorn app:app" > Procfile

8. create git repo
  git init 
9. .gitignore
  echo venv > .gitignore
	echo __pycache__ >> .gitignore
  
10. git add .
11. git commit -m "First Commit"
12 . heroku login 
13. heroku create <name-app>
14 . git push heroku master 




