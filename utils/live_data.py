import pandas as pd
import numpy as np
from datetime import datetime

def generate_live_data():
    current_time = datetime.now()

    usage = round(np.random.uniform(1.5, 8.5), 2)      # kWh
    voltage = round(np.random.uniform(220, 240), 2)    # Volts
    current = round(np.random.uniform(5, 15), 2)       # Amps

    data = {
        "Time": [current_time.strftime("%H:%M:%S")],
        "Usage_kWh": [usage],
        "Voltage": [voltage],
        "Current": [current]
    }

    return pd.DataFrame(data)