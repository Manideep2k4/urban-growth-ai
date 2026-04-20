location_coords = {
    "Whitefield": [77.7500, 12.9698],
    "Indira Nagar": [77.6408, 12.9719],
    "BTM": [77.6101, 12.9166],
    "Electronic City": [77.6603, 12.8399],
    "Yelahanka": [77.5963, 13.1007],
    "Marathahalli": [77.6974, 12.9591]
}

def get_coordinates(location):
    return location_coords.get(location, [77.59, 12.97])  # default Bangalore