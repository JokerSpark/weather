import requests
from flask import Flask,render_template,request
import pandas as pd





app = Flask(__name__)
 
@app.route('/',methods=['POST', 'GET'])
def hello_world():
    api_key = '271d1234d3f497eed5b1d80a07b3fcd1'
    if request.method == 'POST':
        place = request.form['place']   
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')
        # print(weather_data.json())
        coordinates = weather_data.json()['coord'] 
        country = weather_data.json()['sys']['country']  
        temp = round((weather_data.json()['main']['temp'])-273.15,2)
        weather = weather_data.json()['weather'][0]['main']
        return render_template('index.html',coordinates=coordinates,country=country,temp=temp,weather=weather,place=place)  
    return render_template('index.html')






if __name__ == '__main__':
    app.run()

# api_key = '271d1234d3f497eed5b1d80a07b3fcd1'
# place = 'madurai'
# weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')

# print(weather_data.json()!=place)