from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open('saved_model.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
      longitude = float(request.form['longitude'])  
      latitude = float(request.form['latitude'])  
      housing_median_age = float(request.form['housing_median_age'])
      total_rooms = float(request.form['total_rooms'])  
      total_bedrooms = float(request.form['total_bedrooms'])
      population = float(request.form['population'])
      households = float(request.form['households'])
      median_income = float(request.form['median_income'])
      H_OCEAN = float(request.form['H_OCEAN'])
      INLAND = float(request.form['INLAND'])
      ISLAND = float(request.form['ISLAND'])
      NEAR_BAY = float(request.form['NEAR_BAY'])
      NEAR_OCEAN = float(request.form['NEAR_OCEAN'])
      result = model.predict([[longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,H_OCEAN,INLAND,ISLAND,NEAR_BAY,NEAR_OCEAN]])[0]
      return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)      