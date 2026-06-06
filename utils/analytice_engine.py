import pandas as pd
import numpy as np

def compute_trend(data_dict):
    """
    data_dict: dict with keys 'dates' (list of date strings) and 'scores' (list of floats)
    Returns predicted next 3 points using exponential smoothing (simple demo).
    """
    scores = pd.Series(data_dict['scores'])
    smoothed = scores.ewm(span=5).mean()
    last = smoothed.iloc[-1]
    trend = smoothed.diff().mean()
    forecast = [last + trend * i for i in range(1, 4)]
    return forecast
