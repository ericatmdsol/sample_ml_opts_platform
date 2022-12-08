from flask import Flask, request, jsonify
from joblib import dump, load
import pandas as pd
import json

app = Flask(__name__)
app.config["DEBUG"] = True

# extensions aren't that important
# but useful to know what kind of pickling
# lib you used

# the try and except is primarily for loading the model from two 
# different locations
try: 
    model = load('../basic_ml_model/model.jobpkl')
except:
    model = load('/model/model.jobpkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if isinstance(request.json, dict):
        data = [data]
    
    df = pd.DataFrame(data)
    print(df)
    output = model.predict(df)
    output = json.dumps(list(output))
    return(output)

app.run(host="0.0.0.0")