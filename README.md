# Air Quality Prediction — End-to-End Machine Learning Pipeline

## Overview
This project focuses on building an end-to-end machine learning pipeline to predict air quality metrics using environmental data collected from multiple sources.

Unlike previous projects with ready-made datasets, this project required **data acquisition, preprocessing, modeling, and deployment**, simulating a real-world ML workflow.

---

## Data Collection
- Raw environmental data was fetched and aggregated programmatically
- No pre-cleaned dataset was provided
- Data required preprocessing, validation, and feature engineering before modeling

---

## Dataset
- Dataset size: ~6,000 samples × 9 features
- Target: Air quality indicator (regression task)

Due to data generation and aggregation, the dataset exhibits natural variability across runs.

---

## Approach
The project followed a full production-style ML pipeline:

- Data collection and cleaning
- Feature engineering and preprocessing
- Model training and evaluation
- Performance monitoring using regression metrics
- Deployment via a Flask API

---

## Model
- Machine learning regression model
- Preprocessing pipeline including scaling and encoding
- Evaluation using regression metrics (MAE)

---

## Results
- **Mean Absolute Error (MAE): ~2.8–3.1**

Performance varies slightly due to dynamic data generation, reflecting real-world conditions.

---

## Deployment
- A Flask API was implemented to serve model predictions
- The API integrates preprocessing, model inference, and response handling
- Enables real-time prediction via HTTP requests

---

## Tools & Technologies
Python, pandas, NumPy, scikit-learn, matplotlib, Flask, Git, GitHub

---

## Key Takeaways
- Built a complete ML pipeline from raw data to deployed model
- Gained experience with data ingestion and preprocessing challenges
- Demonstrated practical model deployment using Flask
- Highlighted real-world variability in ML performance

This project demonstrates readiness for production-oriented data science and machine learning roles.
