import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

df = df[['location', 'total_sqft', 'bath', 'price']]
df = df.dropna()

def convert_sqft(x):
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df = df.dropna()

df['location'] = df['location'].astype('category')
location_map = dict(enumerate(df['location'].cat.categories))
df['location'] = df['location'].cat.codes

X = df[['location', 'total_sqft', 'bath']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(location_map, open('location_map.pkl', 'wb'))

print("Model trained!")