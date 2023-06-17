import requests 

API_KEY="879c06bd326a87da4ffc25cdacf6a1ea"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code == 200 :
    data = response.json()
    weather = data['weather']
  
 
else:
    print("An error occurred ! ")