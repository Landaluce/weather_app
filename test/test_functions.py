from functions import create_url, get_api_response, get_city_info, create_output


def test_create_url():
    assert create_url(
        3440696, 'metric') == \
        'https://api.openweathermap.org/data/2.5/weather?id=3440696&units=metric&appid=885cd01d1e5002e824cbe4eb0f5ccb2f'


def test_get_api_response():
    response = get_api_response(
        'https://api.openweathermap.org/data/2.5/weather?id=3440696&units=metric&appid=885cd01d1e5002e824cbe4eb0f5ccb2f'
    )
    assert response.status_code == 200


def test_get_city_info():
    result = get_city_info(3440696, {'city_id': '3440696', 'progress': 100.0})
    assert str(result[0])[:21] == "{'city_id': '3440696'"
    assert result[1] == 3440696
    assert result[2] is False


def test_create_output():
    assert create_output('weather.db') == "[{'unique_id': '3440696', 'date_time': '06/07/2021 11:00:36', 'city_info':" \
                                          " '{\"city_id\": \"3440696\", \"progress\": 100.0, \"Temperature\": 15.1," \
                                          " \"Humidity\": 77}'}]"
