import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🌍 Coordinates for Gwalior
latitude = 26.2183
longitude = 78.1828

# 📦 Open-Meteo API URL
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m,relative_humidity_2m"
    f"&timezone=auto"
)

# 🔗 Fetch data
response = requests.get(url)
data = response.json()

# 📊 Convert to DataFrame
df = pd.DataFrame({
    "datetime": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"]
})
df["datetime"] = pd.to_datetime(df["datetime"])

# 🎨 Set Seaborn theme
sns.set_theme(style="darkgrid")

# 🌡️ Temperature Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x="datetime", y="temperature", data=df, label="Temperature (°C)", color="tomato")
plt.title("Hourly Temperature Forecast - Gwalior")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# 💧 Humidity Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x="datetime", y="humidity", data=df, label="Humidity (%)", color="teal")
plt.title("Hourly Humidity Forecast - Gwalior")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
