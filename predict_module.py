import pickle
import pandas as pd


with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)


with open("scaler.pkl", "rb") as f:
    sc = pickle.load(f)

def pm25_to_aqi(pm25):
    breakpoints = [
        (0.0, 12.0, 0, 50),
        (12.1, 35.4, 51, 100),
        (35.5, 55.4, 101, 150),
        (55.5, 150.4, 151, 200),
        (150.5, 250.4, 201, 300),
        (250.5, 350.4, 301, 400),
        (350.5, 500.4, 401, 500)
    ]

    for (bp_lo, bp_hi, aqi_lo, aqi_hi) in breakpoints:
        if bp_lo <= pm25 <= bp_hi:
            return ((aqi_hi - aqi_lo) / (bp_hi - bp_lo)) * (pm25 - bp_lo) + aqi_lo

    return None

def aqi_to_category(aqi):
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Moderate"
    elif aqi <= 150: return "Unhealthy for sensitive groups"
    elif aqi <= 200: return "Unhealthy"
    elif aqi <= 300: return "Very unhealthy"
    else: return "Hazardous"


def get_recom(category):
    rec = {
        "Good": "Air is clean. No restrictions.",
        "Moderate": "Sensitive people should limit outdoor exertion",
        "Unhealthy for sensitive groups": "Wear a mask if you have respiratory issues; limit prolonged outdoor activity.",
        "Unhealthy": "Reduce outdoor activities, wear a mask",
        "Very unhealthy": "Avoid outdoor activites. Wear a good mask",
        "Hazardous": "Stay indoors; go out only if necessary"
    }
    return rec[category]

def anomaly(pm, month):
    return pm / 50

feature_order = [
    'carbon_monoxide',
    'nitrogen_dioxide',
    'sulphur_dioxide',
    'ozone',
    'temperature_2m',
    'relative_humidity_2m',
    'wind_speed_10m',
    'pressure_msl',
    'hour',
    'day_of_week',
    'month'
]

def predict_aqi(input_data):

    X = pd.DataFrame([input_data], columns=feature_order)
    X_scaled = sc.transform(X)
    
    pm25_pred = model.predict(X_scaled)[0]
    aqi = pm25_to_aqi(pm25_pred)
    category = aqi_to_category(aqi)
    rec = get_recom(category)
    anomaly_res = anomaly(pm25_pred, input_data["month"])

    return {
        "pm25_pred": round(pm25_pred, 2),
        "AQI": round(aqi, 2),
        "AQI_category": category,
        "Recommendation": rec,
        "anomaly_factor": round(anomaly_res, 2)
    }
