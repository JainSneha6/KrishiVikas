# 🌾 Krishi Vikas  
**An AI-Powered Farmer Assist Platform**

---

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
- **AgriBERT-powered** suggestions tailored to location, weather patterns, and soil type  
- Interactive **crop calendar** with sowing/harvest timelines and best-practice steps  

### 2️⃣ Plant Disease Identification  
- **CNN-based** image classifier: upload a leaf photo and get instant disease diagnosis  
- Pesticide and treatment recommendations based on model output  

### 3️⃣ Precision Yield Forecasting  
- **SVM-driven** prediction using inputs like land area, fertilizer usage, and historical yields  
- Integrated advice on **crop rotation**, **irrigation scheduling**, and **input optimization**  

### 4️⃣ Market Price Forecasting  
- **Time-series forecasting** (SARIMA) for crop prices and demand trends  
- Dynamic charts to plan optimal selling windows  

### 5️⃣ Crowdsourced Problem Reporting  
- **Geo-spatial mapping** via DBSCAN for incident location  
- **K-means & NLP** for problem categorization  
- Severity scoring through rule-based + ML classification  

### 6️⃣ KrishiSahayak Chatbot  
- AI-chat interface offering **alternative income** paths:  
  Horticulture, Apiculture, Dairy, Poultry, Goat & Sheep Rearing, Agro-Tourism, and more  
- Multilingual & voice-enabled support for non-literate users  

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


