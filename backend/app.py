from flask import Flask, request, jsonify
import requests
import google.generativeai as genai
from flask_cors import CORS
import re
from deep_translator import GoogleTranslator  
import os
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import timedelta

app = Flask(__name__)
CORS(app)

# API Keys
WEATHER_API_KEY = 'f28861253e574c589d5111924242807'
GEMINI_API_KEY = 'AIzaSyDNOtokPHTUm9WCJ1pOPaweUp_Rks9DhjI'
UNSPLASH_ACCESS_KEY = 'YAd-Af7cIyfplIFBCWaKRL1XiNE6VsFULmx-ln-_HfY'

# Initialize Gemini Model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

app.config['UPLOAD_FOLDER'] = './uploads' 

@app.route('/recommendations', methods=['POST'])
def recommendations():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    category = data.get('category')
    lang = data.get('language', 'en')  # Default to English

    if not lat or not lon or not category:
        return jsonify({'error': 'Latitude, Longitude, and Category are required'}), 400

    weather_data = get_weather_data(lat, lon)
    if not weather_data:
        return jsonify({'error': 'Failed to get weather data'}), 500

    recommendations = get_crop_recommendations(weather_data, category, lang)
    if not recommendations:
        return jsonify({'error': 'Failed to get crop recommendations'}), 500

    return jsonify({"Recommendations": recommendations})

def get_crop_recommendations(weather_data, category, lang):
    try:
        query = f"Generate 5 crop recommendations for the category: {category} given the weather conditions: {weather_data}. Give me only the name with one line information."
        
        # AI Model Response
        response = model.generate_content(query)
        recommendations_text = response.text.strip()

        # Extract names and descriptions using regex
        pattern = re.compile(r'\d+\.\s*([^\:]+):\s*([^\n]+)')
        matches = pattern.findall(recommendations_text)

        translated_recommendations = []
        for match in matches:
            name = match[0].strip().replace('**', '')
            ename = name  # English name
            description = match[1].strip().replace('**', '')
            image = get_crop_image(name)

            if lang != 'en':
                name = translate_text(name, lang)
                description = translate_text(description, lang)

            translated_recommendations.append({
                'name': name,
                'ename': ename,
                'description': description,
                'image': image
            })

        return translated_recommendations
    except Exception as e:
        print(f"Error generating crop recommendations: {e}")
        return []

def translate_text(text, lang):
    """Translate text using Deep Translator."""
    try:
        return GoogleTranslator(source='auto', target=lang).translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text if translation fails

def get_crop_image(crop_name):
    """Fetch crop images from Unsplash API."""
    url = f"https://api.unsplash.com/search/photos?query={crop_name}&client_id={UNSPLASH_ACCESS_KEY}&per_page=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['results'][0]['urls']['small'] if data['results'] else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image for {crop_name}: {e}")
        return None

def get_weather_data(lat, lon):
    """Fetch weather data from WeatherAPI."""
    url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={lat},{lon}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    
@app.route('/crop_steps', methods=['POST'])
def crop_steps():
    data = request.json
    crop_name = data.get('crop_name')
    lang = data.get('language', 'en')
    category = data.get('category')

    if not crop_name:
        return jsonify({'error': 'Crop name is required'}), 400
    
    if lang != 'en':
        crop_name = translate_text(crop_name, lang)

    try:
        if category:
            queries = [f"Give me a small paragraph on {category} for {crop_name} in language {lang}"]

        response = model.generate_content(queries)
        recommendations_text = response.text 
        return(recommendations_text)
    

    except Exception as e:
        print(f"Error generating crop growing steps: {e}")
        return jsonify({'error': 'Failed to get crop growing steps'}), 500

@app.route('/predict-disease', methods=['POST'])
def predict_disease():
    if 'image' not in request.files:
        return jsonify({'error': 'Image is required'}), 400

    try:
        image = request.files['image']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
        image.save(image_path.replace('\\','/'))
        
        # Open the image and convert it to bytes
        with open(image_path, 'rb') as img_file:
            img_bytes = img_file.read()

        # Send image to Gemini AI model for disease prediction
        response = genai.upload_file(path=image_path)  # Ensure this function is defined
        prompt = "Identify the plant disease in this image and provide the result in plain text."
        prediction_response = model.generate_content([response, prompt]) 
        
        match = re.search(r'\\(.?)\\*', prediction_response.text)
        
        if match:
            return jsonify({'prediction': match.group(1)})
        else:
            return jsonify({'prediction': prediction_response.text})
        
    except Exception as e:
        print(f"Error making prediction with Gemini AI: {e}")
        return jsonify({'error': 'Failed to make prediction'}), 500
    
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    lang = data.get('language', 'en')
    query = data.get('query')
    
    if lang != 'en':
        query = translate_text(query, lang)

    try:
        if query:
            queries = [f"Give me the answer for this query {query} in language {lang}. The query should be related to only farming related stuff. In case of any other irrelevant question just say something like I am KrishiSahayak and will answer to only farming related stuff. In case of queries like diseases of crops, ask them to go to CNN Enabled Plant Disease Identification of the same website KrishiVikas"]

        response = model.generate_content(queries)
        recommendations_text = response.text 
        
        recommendations_text = recommendations_text.replace("**","")
        recommendations_text = recommendations_text.replace("*","-")
        return(recommendations_text)

    except Exception as e:
        print(f"Error generating answers: {e}")
        return jsonify({'error': 'Failed to get answers'}), 500

def get_weather_forecast(lat, lon):
    """Fetch 7-day weather forecast from WeatherAPI."""
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={lat},{lon}&days=7"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather forecast: {e}")
        return None

@app.route("/weather-forecast", methods=["POST"])
def weather_forecast():
    """API endpoint to fetch 7-day weather forecast."""
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    forecast_data = get_weather_forecast(lat, lon)
    if forecast_data:
        return jsonify(forecast_data)
    else:
        return jsonify({"error": "Failed to fetch weather forecast"}), 500

@app.route('/crop-calendar', methods=['POST'])
def generate_crop_calendar():
    try:
        # Parse the request data from the React frontend
        data = request.json
        if not data or "cropName" not in data or "latitude" not in data or "longitude" not in data:
            return jsonify({"message": "Invalid data provided"}), 400

        # Extract crop name and location details
        crop_name = data["cropName"].strip()
        latitude = data["latitude"]
        longitude = data["longitude"]
        lang=data["lang"]

        if not crop_name:
            return jsonify({"message": "Crop name is required"}), 400
        
        weather_data = get_weather_data(latitude, longitude)
        if not weather_data:
            return jsonify({'error': 'Failed to get weather data'}), 500

        # Generate a precise and structured AI prompt
        prompt = (
            f"You are an expert agronomist. Generate a **detailed crop calendar** for {crop_name} based on {weather_data} in this language {lang}."
            f"based on the location (Latitude: {latitude}, Longitude: {longitude}) in India. "
            f"Ensure it follows best farming practices suited for the region. The response should "
            f"be **structured and formatted** so that each stage is clearly separated. Use double asterisks (**) "
            f"to highlight stage titles. Keep each section detailed and concise.\n\n"
            f"### Crop Calendar for {crop_name} ({latitude}, {longitude})\n"
            f"1. **Land Preparation**\n   - Time:\n   - Activities:\n"
            f"2. **Seed Treatment**\n   - Time:\n   - Method:\n   - Chemicals Used:\n"
            f"3. **Sowing Period**\n   - Best Months:\n   - Method:\n"
            f"4. **Irrigation Schedule**\n   - Frequency:\n   - Best Practices:\n"
            f"5. **Fertilization Schedule**\n   - Types of Fertilizers:\n   - Application Timing:\n"
            f"6. **Weed Management**\n   - Techniques:\n   - Chemicals Used:\n"
            f"7. **Pest & Disease Management**\n   - Common Pests & Diseases:\n   - Control Methods:\n"
            f"8. **Harvesting Time**\n   - Month:\n   - Harvesting Methods:\n"
            f"9. **Post-Harvest Handling**\n   - Storage & Processing Tips:\n\n"
            f"Make sure the response follows this structured format so that each stage is **clearly extractable**."
        )

        # Generate response using AI model
        response = model.generate_content([prompt])
        crop_calendar_text = response.text
        crop_calendar_text = crop_calendar_text.replace("**","")
        crop_calendar_text = crop_calendar_text.replace("###","")
        

        # Respond to the frontend with the structured crop calendar
        return jsonify({"cropCalendar": crop_calendar_text}), 200

    except Exception as e:
        print(f"Error while generating crop calendar: {e}")
        return jsonify({"message": "Error generating crop calendar"}), 500
    
df = pd.read_csv('../data/crop_sales_data.csv', parse_dates=['Date'])

# 2) Pre-calculate best and worst sellers
crop_sums = df.groupby('Crop')['Quantity Sold (kg)'].sum().sort_values(ascending=False)
top_3_crops = crop_sums.head(3)
bottom_3_crops = crop_sums.tail(3)

@app.route('/best_worst_sellers', methods=['GET'])
def best_worst_sellers():
    """
    Returns the top 3 and bottom 3 crops by total quantity sold.
    """
    best_sellers_df = top_3_crops.reset_index().rename(columns={'Quantity Sold (kg)': 'TotalSales'})
    worst_sellers_df = bottom_3_crops.reset_index().rename(columns={'Quantity Sold (kg)': 'TotalSales'})
    
    response = {
        'best_sellers': best_sellers_df.to_dict(orient='records'),
        'worst_sellers': worst_sellers_df.to_dict(orient='records')
    }
    return jsonify(response)

@app.route('/forecast', methods=['GET'])
def forecast():
    """
    Generate future forecast for a selected crop using SARIMAX.
    Query params: /forecast?crop=Rice&periods=7
    """
    crop_name = request.args.get('crop', 'Rice')
    periods = request.args.get('periods', 7, type=int)
    
    # Filter data for selected crop
    crop_data = df[df['Crop'] == crop_name].copy()
    crop_data.sort_values(by='Date', inplace=True)
    crop_data.set_index('Date', inplace=True)

    if len(crop_data) < 5:
        return jsonify({'error': 'Not enough data to forecast for this crop.'}), 400

    y = crop_data['Quantity Sold (kg)']
    
    # A simple, placeholder SARIMAX configuration
    model = SARIMAX(y, 
                    order=(1,1,1),
                    seasonal_order=(1,1,1,7),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    results = model.fit(disp=False)
    
    # Forecast for given periods
    forecast_values = results.predict(start=len(y), end=len(y)+periods-1, typ='levels').tolist()
    
    # Generate future dates
    last_date = crop_data.index[-1]
    future_dates = [last_date + timedelta(days=i) for i in range(1, periods+1)]
    
    forecast_output = []
    for date, val in zip(future_dates, forecast_values):
        forecast_output.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Forecast': round(val, 2)
        })

    # Return last 7 days of actual data + forecast for easier charting
    historical_df = crop_data.tail(7).reset_index()
    historical_df['Date'] = historical_df['Date'].dt.strftime('%Y-%m-%d')
    historical_output = historical_df[['Date', 'Quantity Sold (kg)']]\
                                     .rename(columns={'Quantity Sold (kg)': 'Actual'})

    response = {
        'crop': crop_name,
        'historical': historical_output.to_dict(orient='records'),
        'forecast': forecast_output
    }
    return jsonify(response)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
