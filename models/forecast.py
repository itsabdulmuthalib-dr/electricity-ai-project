import numpy as np

def predict_next_usage(history):
    values = history["Usage_kWh"].values

    if len(values) < 3:
        return round(values[-1], 2)

    prediction = np.mean(values[-3:])
    return round(prediction, 2)