import pickle

model = pickle.load(open("model.pkl", "rb"))
location_map = pickle.load(open("location_map.pkl", "rb"))

# Reverse mapping
reverse_map = {v: k for k, v in location_map.items()}

def get_location_code(name):
    for code, loc in location_map.items():
        if str(loc).lower() == name.lower():
            return code
    return 0  # default fallback

def predict_price(location_name, sqft, bath):
    loc_code = get_location_code(location_name)
    return model.predict([[loc_code, sqft, bath]])[0]

def predict_future(price):
    return round(price * (1.1 ** 3), 2)