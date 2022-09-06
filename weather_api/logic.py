import requests


def enter_city():
    city = input("Enter city: ")
    if not city:
        print("Sorry city name must be entered")
        exit()
    return city


def get_url(base_url, api_key, city_name):
    url = f"{base_url}appid={api_key}&q={city_name}"
    return url


def get_response(url):
    response = requests.get(url).json()
    return response


def kelvin_to_celsius(kelvin: float) -> float:
    celsius = kelvin - 273.15
    return celsius


def get_info(response):
    try:
        temp_kelvin = response['main']['temp']
    except KeyError:
        print("Not valid input")
        exit()
    else:
        wind_speed = response['wind']['speed']
        temp_celsius = kelvin_to_celsius(temp_kelvin)

        return {
            ("temperature is " + f"{temp_celsius}" + " celsius"),
            ("wind speed is " + f"{wind_speed}")
        }
