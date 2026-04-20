import pandas as pd

def convert_sqft(x):
    try:
        if isinstance(x, str):
            if '-' in x:
                tokens = x.split('-')
                return (float(tokens[0]) + float(tokens[1])) / 2
            return float(x)
        return float(x)
    except:
        return None

def calculate_growth(df):
    # Convert columns safely
    df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
    df['bath'] = pd.to_numeric(df['bath'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Drop invalid rows
    df = df.dropna()

    # Growth calculations
    df['price_change'] = df['price'].pct_change().fillna(0)
    df['demand'] = df['total_sqft'] / (df['bath'] + 1)

    df['growth_score'] = (
        0.6 * df['price_change'] +
        0.3 * df['demand'] +
        0.1 * df['bath']
    )

    return df[['location', 'growth_score']]