import time
import json
import requests
from datetime import datetime
from constants import api_key
from database_manager import create_connection


def create_url(city_id, units):
    return "https://api.openweathermap.org/data/2.5/weather?id=%s&units=%s&appid=%s" % (city_id, units, api_key)


def get_api_response(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(str(e))
        time.sleep(60)
        response = requests.get(url)
    print(response)
    return response


def get_city_info(city_id, city_info, units='metric'):
    response = get_api_response(create_url(city_id, units))
    data = json.loads(response.text)
    error_code = 404
    if response.status_code != error_code:
        city_info['Temperature'] = data['main']['temp']
        city_info['Humidity'] = data['main']['humidity']
        error = False
    else:
        city_info['Temperature'] = 0
        city_info['Humidity'] = 0
        error = True
    return city_info, city_id, error


def create_output(db_file='weather.db'):
    connection, cursor = create_connection(db_file)
    cursor.execute("SELECT * FROM weather_app")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    results = []
    for row in rows:
        result = {
            'unique_id': row[0],
            'date_time': row[1],
            'city_info': row[2],
        }
        results.append(result)
    print(results)
    return str(results)


async def get_weather_info(city_info, db_file='weather.db'):
    city_id = city_info['city_id']
    date_time_format = "%d/%m/%Y %H:%M:%S"
    connection, cursor = create_connection(db_file)
    cursor.execute('CREATE TABLE IF NOT EXISTS weather_app (u_id TEXT, date_time TEXT, city_info TEXT)')
    connection.commit()
    connection.close()
    connection, cursor = create_connection(db_file)
    cursor.execute("SELECT u_id FROM weather_app WHERE u_id =" + str(city_id))
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    if not len(data):
        city_info, u_id, error = get_city_info(city_id, city_info)
        if not error:
            date_time = datetime.now().strftime(date_time_format)
            connection, cursor = create_connection(db_file)
            cursor.execute(
                "INSERT INTO weather_app (u_id, date_time, city_info) VALUES (?, ?, ?);",
                (u_id, date_time, json.dumps(city_info)))
            connection.commit()
            connection.close()
    return create_output(db_file)
