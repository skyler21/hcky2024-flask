from flask import Flask,render_template
import sys
import os
import logging
import http.client
import urllib3
import json


logging.basicConfig(stream=sys.stdout, 
    format='%(asctime)s|%(levelname)s|%(thread)s|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG)

serviceName = 'hockey2024app-hockey-service'
servicePort = 8085

logging.info(f"Service URL and Port: {serviceName}:{servicePort}")

https = urllib3.PoolManager()


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
    
@app.route("/getTeams")
def getTeams():
  
  url = f"http://{serviceName}:{servicePort}/db/get/teams"

  resp = https.request('GET', url)
  print("Response Status = " + str(resp.status))
  print("Response DATA = " + str(resp.data))
  print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("teams.html", len = len(json_html), json_html = json_html) 
   
  app.run(use_reloader = True, debug = True) 

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
