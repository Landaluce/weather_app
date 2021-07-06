##Instructions:

1. Install Python3 and pip [see here how](https://docs.python-guide.org/starting/install3/linux/)
2. Create a free account at [Open Weather Map](https://home.openweathermap.org/) and create an API key
3. In weather_app/constants.py: replace the Xes with your API key
4. Follow method 1 or method 2 bellow

###Method 1:
* In your Terminal
* Go to weather_app/
* run this command:```sudo docker build -t weather_app ```
* Then: ```sudo docker run --name weather -p 5000:5000 weather```

or

###Method 2:
* In your Terminal
* Go to weather_app/
* run this command: ```pip install -r requirements.tx```
* then: ``` python3 main.py```
