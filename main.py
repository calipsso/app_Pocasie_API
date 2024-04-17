import requests

def get_weather_data(city):
    api_key = '673271932b254c849a5201250241704'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'Chyba pri volaní API: {e}')
        return None

city = input("Zadaj mesto: ")
weather_data = get_weather_data(city)

if weather_data:
    temperature_celsius = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    print(f'Aktuálne počasie v {city}: Teplota: {temperature_celsius} °C, Stav: {condition}')
else:
    print('Nepodarilo sa získať informácie o počasí.')