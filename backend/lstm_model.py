import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_lstm():
    data = np.sin(np.linspace(0, 50, 1000))  # simulated trend

    X, y = [], []
    for i in range(10, len(data)):
        X.append(data[i-10:i])
        y.append(data[i])

    X = np.array(X)
    y = np.array(y)

    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = Sequential([
        LSTM(50, return_sequences=False, input_shape=(10,1)),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=3)

    model.save("lstm.h5")
    print("LSTM trained")