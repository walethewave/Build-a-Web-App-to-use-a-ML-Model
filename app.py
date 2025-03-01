# app.py
from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pickle
import numpy as np
from functools import lru_cache

app = Flask(__name__)

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Load model and encoder
with open('ufo-model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

# Cache predictions
@lru_cache(maxsize=100)
def cached_predict(seconds: float, lat: float, lon: float):
    return model.predict([[seconds, lat, lon]])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")
def predict():
    try:
        # Validate inputs
        seconds = float(request.form['seconds'])
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])
        
        if not (1 <= seconds <= 60):
            raise ValueError("Seconds must be between 1-60")
        if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
            raise ValueError("Invalid coordinates")
            
        # Get prediction
        pred_code = cached_predict(seconds, lat, lon)
        country = le.inverse_transform(pred_code)[0]
        
        return render_template('index.html',
            prediction_text=f'Likely country: {country}'
        )
        
    except Exception as e:
        return render_template('index.html',
            prediction_text=f'Error: {str(e)}'
        )

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_version': '1.1.0',
        'supported_countries': list(le.classes_)
    })

if __name__ == '__main__':
    app.run(debug=True)
    
    # Required for Vercel serverless deployment
application = app  # Vercel looks for 'application' by default

