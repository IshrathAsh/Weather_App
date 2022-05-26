import datetime
import requests,json
from flask import Flask, render_template, redirect,request

app = Flask(__name__)
 
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/weather',methods=[ "POST"])
def weather():    
    city= request.form.get("city")

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3624231d298e7581f8bf84e775eff328"
    
    req= requests.get(url.format(city)).json()
 
    result ={     
       "city" : city,
       "description" : req.get("weather")[0].get("description"),
       "temp" : (req.get("main").get("temp")-32)*5/9,
       "humidity" : req.get("main").get("humidity"),
       "img" : "http://openweathermap.org/img/w/" + req.get("weather")[0].get("icon") + ".png"
       }
    return render_template('weather.html', result=result)


if __name__ =='__main__':  
  app.run(debug = True) 

 
 