import requests
import numpy as np

r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.56939&longitude=2.65024&hourly=temperature_2m")
if r.status_code == 200:
   data = r.json()
   if "hourly" in data and "temperature_2m" in data["hourly"]:
      mean_temp = np.mean(data["hourly"]["temperature_2m"])
      print("{:2f} avg temperature".format(mean_temp))
   else:
      print("No hourly data found!")
else:
   print("Error response code {}".format(r.status_code))