from logic import get_info, get_response, get_url, enter_city
from __init__ import API_KEY, BASE_URL


def main():
    city_name = enter_city()
    url = get_url(BASE_URL, API_KEY, city_name)
    resp = get_response(url)
    result = get_info(resp)
    return result


if __name__ == '__main__':
    print(main())
