#%%
import requests
import pandas as pd
from io import StringIO
import time
import random

URL = "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_13012026.csv"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/csv,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(HEADERS)

# 1️⃣ Warm-up request (VERY IMPORTANT)
session.get("https://www.nseindia.com", timeout=10)
time.sleep(random.uniform(1.5, 3.0))

# 2️⃣ Actual CSV request
response = session.get(URL, timeout=20)
response.raise_for_status()

# 3️⃣ Load into DataFrame
df = pd.read_csv(StringIO(response.text))

print(df.head())
print("Rows:", len(df))


# %%


