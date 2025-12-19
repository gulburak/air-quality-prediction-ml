from flask import Flask, render_template, request, jsonify
from predict_module import predict_aqi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_aq1.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    input_data = {
        "carbon_monoxide": data.get("carbon_monoxide", 4.2),
        "nitrogen_dioxide": data.get("nitrogen_dioxide", 55.0),
        "sulphur_dioxide": data.get("sulphur_dioxide", 35.0),
        "ozone": data.get("ozone", 50.0),
        "temperature_2m": data.get("temperature_2m", 20),
        "relative_humidity_2m": data.get("relative_humidity_2m", 50),
        "wind_speed_10m": data.get("wind_speed_10m", 2),
        "pressure_msl": data.get("pressure_msl", 1013),
        "hour": data.get("hour", 12),
        "day_of_week": data.get("day_of_week", 3),
        "month": data.get("month", 1)
    }

    result = predict_aqi(input_data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)


