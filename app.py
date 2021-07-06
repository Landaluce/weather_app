import asyncio
from flask import Flask, request, render_template
from functions import get_weather_info
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        ids = request.form.get("ids")
        ids = ids.split(', ')
        count = 0.0
        result = ''
        all_info = []
        for u_id in ids:
            count += 1.0
            progress = round(count / len(ids) * 100, 2)
            city_info = {'city_id': u_id, 'progress': progress}
            info = asyncio.run(get_weather_info(city_info))
            all_info.append(info)
            result = info
        return result
    return render_template("form.html")


if __name__ == '__main__':
    app.run(host ='127.0.0.1', port=5000, debug=True)
