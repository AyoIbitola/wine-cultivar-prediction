from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load Model and Scaler
MODEL_PATH = os.path.join('model', 'wine_cultivar_model.pkl')
SCALER_PATH = os.path.join('model', 'scaler.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and Scaler loaded successfully.")
except FileNotFoundError:
    print("Error: Model or Scaler file not found. Please train the model first.")
    model = None
    scaler = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ""
    if request.method == 'POST':
        if not model or not scaler:
            return render_template('index.html', prediction_text="Error: Model not loaded.")
        
        try:
            # Get values from form
            features = [
                float(request.form['alcohol']),
                float(request.form['flavanoids']),
                float(request.form['color_intensity']),
                float(request.form['hue']),
                float(request.form['proline']),
                float(request.form['od280'])
            ]
            
            # Preprocess
            features_array = np.array([features])
            features_scaled = scaler.transform(features_array)
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            
            # Map prediction to Cultivar Name (dataset target is 0, 1, 2)
            # Cultivars are usually 1, 2, 3 in the UCI dataset description, 
            # but sklearn loads them as integers 0, 1, 2.
            cultivar_map = {0: "Cultivar 1", 1: "Cultivar 2", 2: "Cultivar 3"}
            predicted_class = cultivar_map.get(prediction, f"Unknown ({prediction})")
            
            prediction_text = f"Predicted Origin: {predicted_class}"
            
        except ValueError:
            prediction_text = "Error: Please enter valid numerical values."
        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
