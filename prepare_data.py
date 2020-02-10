import pandas as pd

from config import CONFIG

# Get emissions data
df = pd.read_csv(CONFIG["emissions-path"])
