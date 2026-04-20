from flask import Flask, request, jsonify
import pandas as pd
from model import predict_price, predict_future
from growth_model import calculate_growth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    location = data["location"]   # now string
    sqft = float(data["sqft"])
    bath = int(data["bath"])

    price = predict_price(location, sqft, bath)
    future = predict_future(price)

    return jsonify({
        "current_price": round(price, 2),
        "future_price": future
    })

@app.route("/growth", methods=["GET"])
def growth():
    df = pd.read_csv("data.csv")
    df = df[['location', 'total_sqft', 'bath', 'price']]

    g = calculate_growth(df)

    result = []
    for _, row in g.iterrows():
        coords = get_coordinates(row['location'])

        result.append({
            "location": row['location'],
            "growth_score": float(row['growth_score']),
            "lng": coords[0],
            "lat": coords[1]
        })

    return jsonify(result)
def home():
    return "🚀 Urban Growth AI Backend Running!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)