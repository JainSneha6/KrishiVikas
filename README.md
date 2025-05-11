# 🌾 Krishi Vikas  - An AI-Powered Farmer Assist Platform
---

Krishi Vikas is an AI-powered agricultural platform built to support small and marginal farmers.
It offers personalized crop advice, disease diagnostics, market forecasts, and income alternatives using cutting-edge ML and NLP.
Designed for inclusivity, the platform ensures accessibility through multilingual and voice-enabled interfaces.

## Table of Contents
1. [Overview](#overview)  
2. [Problem Statement](#problem-statement)  
3. [Features](#features)  
4. [Architecture](#architecture)  
5. [Tech Stack](#tech-stack)  
6. [Installation](#installation)  
7. [Usage](#usage)  
8. [Project Structure](#project-structure)  
9. [Models & Data](#models--data)  
10. [Contributing](#contributing)  
11. [License](#license)  
12. [Contact](#contact)  

---

## Overview
**Krishi Vikas** is an end-to-end, AI-driven platform designed to empower small and marginal farmers with smart, data-backed advice at every stage of the crop lifecycle. From choosing the right crop variety for your agro-climatic zone to diagnosing plant diseases, forecasting yield and price, reporting in-field issues, and suggesting alternative income streams—Krishi Vikas brings cutting-edge ML/AI tools into the hands of those who need them most.

---

## Problem Statement

<div align="center">

 <img src="https://github.com/user-attachments/assets/cafffacd-a5e9-49f1-a08e-f025cd1ac6f8"  width="700"/>

</div>

Farmers, especially those managing less than 2 hectares of land, face multiple challenges:

1. **Sub-optimal Crop Selection**  
   Traditional intuition often drives crop choice, ignoring soil, weather, and market factors.

2. **Late or Missed Disease Diagnosis**  
   Visual symptoms go unnoticed or misidentified, leading to crop losses.

3. **Unpredictable Yield & Storage Planning**  
   Lack of accurate yield forecasts hampers storage, finance, and resource planning.

4. **Poor Post-Harvest Price Forecasting**  
   No reliable market trend data leads to sub-optimal selling times.

5. **Invisible In-Field Issues**  
   Pests, nutrient deficiencies, and flooding incidents often remain unreported and unaddressed.

6. **Income Instability**  
   Crop failures leave farmers without alternative livelihood guidance.

---

## Features
<div align="center">

 <img src="https://github.com/user-attachments/assets/b4ab4cfe-12a2-4423-866d-dadc41029e8a"  width="700"/>

</div>


### 1️⃣ Agro-Climatic Crop Recommendation  
🔍 **Description:**  
Farmers receive crop recommendations suited to their region’s climate, soil, and season using a fine-tuned BERT model trained on agricultural domain data (**AgriBERT**). Recommendations also include interactive crop calendars that dynamically adjust for weather forecasts.

🔧 **Tech Stack:**  
- **Frontend:** React (web) / Ionic React (mobile) with calendar visualization libraries (e.g., FullCalendar.js)  
- **Backend:** Flask / FastAPI for model serving  
- **Model:** Fine-tuned AgriBERT (transformer) on labeled agri-domain corpora  
- **Data Sources:** IMD weather APIs, ISRO/Bhuvan soil maps, local agri departments  
- **Database:** PostgreSQL with PostGIS for geospatial queries  

🧠 **How Tech is Used:**  
- Input: Location coordinates, soil type, weather  
- NLP with AgriBERT to understand agronomic advisories  
- Model inference ranks suitable crops  
- Calendar auto-generates crop schedules based on regional climate  


### 2️⃣ Plant Disease Identification  
🔍 **Description:**  
Farmers upload photos of infected leaves. A CNN-based image classifier detects the disease and suggests remedial treatments, including pesticide or organic options.

🔧 **Tech Stack:**  
- **Frontend:** React / Ionic with image upload & preview (Cropper.js)  
- **Backend:** Flask / TensorFlow Serving for model inference  
- **Model:** CNN architecture (e.g., ResNet50 or MobileNet for edge-friendliness)  
- **Database:** MongoDB or Firebase for storing images and metadata  

🧠 **How Tech is Used:**  
- Uploaded leaf image is processed and classified using a CNN  
- Based on the detected disease class, a treatment recommendation engine fetches pesticide info from a curated dataset or API  

### 3️⃣ Precision Yield Forecasting  
🔍 **Description:**  
Uses Support Vector Machines (SVM) trained on historical crop data to predict expected yield. Provides actionable insights such as crop rotation, fertilizer planning, and irrigation schedules.

🔧 **Tech Stack:**  
- **Frontend:** Charts with D3.js or Chart.js for yield visualization  
- **Backend:** Flask + Scikit-learn for SVM modeling  
- **Model:** SVM regressor trained on features like land area, fertilizer quantity, rainfall, etc.  
- **Data Sources:** Agmarknet, ICAR datasets, Farmer-reported data  
- **Database:** MySQL / PostgreSQL  

🧠 **How Tech is Used:**  
- Farmers input data like sowing time, area, inputs used  
- Model returns predicted yield  
- Expert system layer advises on optimization (e.g., nitrogen/phosphorus levels) 

### 4️⃣ Market Price Forecasting  
🔍 **Description:**  
Uses SARIMA (Seasonal AutoRegressive Integrated Moving Average) models for time-series forecasting of crop prices. Helps farmers time their sales for profit maximization.

🔧 **Tech Stack:**  
- **Frontend:** Highcharts or Recharts for trend visualization  
- **Backend:** Python (Statsmodels for SARIMA)  
- **Data Sources:** Agmarknet, eNAM, local mandi feeds  
- **Database:** TimescaleDB (for time-series optimized PostgreSQL)  

🧠 **How Tech is Used:**  
- SARIMA model trained on historical mandi price data  
- User selects crop and region → future price trends displayed  
- Suggests optimal harvest or storage durations  

### 5️⃣ Crowdsourced Problem Reporting  
🔍 **Description:**  
Farmers report issues like pest outbreaks, waterlogging, etc. These are clustered and geo-mapped using DBSCAN and categorized using NLP + K-means. Severity scoring combines ML and rule-based logic.

🔧 **Tech Stack:**  
- **Frontend:** Interactive maps with Leaflet.js or Mapbox  
- **Backend:** Python with Scikit-learn (DBSCAN, K-means), spaCy/NLTK  
- **Geospatial DB:** PostGIS  
- **Storage:** Firebase for real-time sync or MongoDB  

🧠 **How Tech is Used:**  
- Reports submitted via app (text + geolocation)  
- Clustering (DBSCAN) identifies outbreak zones  
- NLP categorizes issue type; severity scored  
- Visual alerts on map + dashboard for authorities  

### 6️⃣ KrishiSahayak Chatbot  
🔍 **Description:**  
AI-powered chatbot assistant that suggests alternative income sources like apiculture or agro-tourism. Supports multilingual, voice, and offline capabilities.

🔧 **Tech Stack:**  
- **Frontend:** Ionic React + Web Speech API (for voice input/output)  
- **Bot Framework:** Rasa / Dialogflow / Microsoft Bot Framework  
- **NLP Model:** BERT / IndicBERT (for Indian language understanding)  
- **Text-to-Speech (TTS):** Google Cloud TTS / Amazon Polly  
- **Languages:** Hindi, Marathi, Tamil, Telugu, Bengali, etc.  

🧠 **How Tech is Used:**  
- Chatbot NLP parses user's request (“How to start poultry farming?”)  
- Fetches curated guides or summarizes from agri knowledge base  
- Offers voice-based interaction for low-literacy users  
- Supports offline mode via PWA and caching FAQs  

---

## Architecture

<div align="center">

 <img src="https://github.com/user-attachments/assets/5a2f5bb6-0d59-4ec2-b27d-1cb994894183"  width="700"/>

</div>

**Flow:**  
1. **Frontend** (React Web + Ionic Mobile)  
2. **Backend** (Flask REST API)  
3. **ML/AI Models** (TensorFlow, scikit-learn, statsmodels)  
4. **Database** for user, farm, and report data  
5. **External APIs** for weather, geolocation, and TTS  


---

## 🌐 Why Diversity is Our Topmost Priority

We focus on inclusivity and accessibility through multilingual support, personalized user targeting, and a tech stack that ensures adaptability across use cases.


<div align="center">
  <img src="https://github.com/user-attachments/assets/2dfc3788-2f11-48db-a93f-94926160e2ec" alt="Diversity and Tech Stack Slide" width="700"/>
</div>

### 🔑 Key Focus Areas:
- **Multilingual Support** with `mBERT` for better regional understanding
- **Voice Assistant** using **Google Text to Speech** for non-literate users
- **User-Centric Design** mapping advice to regional weather and soil types
- **Diverse Feature Set** catering to every farmer's needs

### ⚙️ Tech Stack Overview:
- **Frontend:** React (Web), Ionic (Mobile)
- **Backend:** Flask
- **ML & AI Models:** TensorFlow, Scikit-learn, Python, Statsmodels

> This diverse and inclusive technology stack allows us to reach more users with tailored solutions.

---


## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/JainSneha6/KrishiVikas.git
   cd KrishiVikas
   ```
2. **Backend Setup**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   flask run --host=0.0.0.0 --port=5000
   ```
3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   npm start      # React web on http://localhost:3000
   ionic serve    # Mobile preview
   ```

---


## 📊 Competitor Analysis

We evaluated Krishi-Vikas alongside top AgriTech players—Plantix, Kindwise, and Cropin—across five core features. Our product stands out with comprehensive AI-driven solutions tailored for farmers' diverse needs.


<div align="center">
  <img src="https://github.com/user-attachments/assets/e4531ddb-816f-4f37-964e-6b364bc2c5d8" alt="Competitor Analysis Slide" width="700"/>
</div>

### ✅ Key Advantages of Krishi-Vikas:
- Full-stack AI coverage: from **crop recommendation** to **income advisory**
- Uniquely offers **geo-spatial issue mapping** using crowdsourced data
- Combines **CNN**, **time-series**, and **chatbot tech** in one solution

Krishi-Vikas clearly leads in providing an all-in-one platform for small and marginal farmers.

---


## 🧩 Business Model & 🔍 Research Overview

The following slide presents our business model and research foundation for **Krishi Vikas**:

<div align="center">
  <img src="https://github.com/user-attachments/assets/a99c00f5-84e0-450f-9601-6586217422bd" alt="Business Model and Research Slide" width="700"/>
</div>

 **Key Highlights**  
 - Targeting 86% of Indian farmers (small & marginal).  
 - Cost-efficient model focusing on cloud and marketing.  
 - Research backed by cutting-edge models like AgriBERT, FinBERT, SARIMA, and CNN.  
 - Monetization through B2C access and ad revenue.

### 🔬 Research References  

- **Why AgriBERT?**  
  [Exploring New Frontiers in Agricultural NLP](https://ieeexplore.ieee.org/abstract/document/10637955)

- **Why finBERT?**  
  [Financial Sentiment Analysis on News and Reports Using FinBERT](https://ieeexplore.ieee.org/abstract/document/10796670)

- **Why SARIMA?**  
  [Study and Analysis of SARIMA and LSTM in Forecasting Time Series Data](https://www.sciencedirect.com/science/article/abs/pii/S2213138821004847)

- **Why CNN?**  
  [Classification of Plant Diseases Using Pretrained CNN on ImageNet](https://openagriculturejournal.com/VOLUME/18/ELOCATOR/e18743315305194/FULLTEXT/)


---


