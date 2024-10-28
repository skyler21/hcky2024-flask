from flask import Flask,render_template
import socket
import sys
import os
import logging


logging.basicConfig(stream=sys.stdout, 
    format='%(asctime)s|%(levelname)s|%(thread)s|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG)

self.urlPort = config.HOCKEY2024APP_HOCKEY_SERVICE_PORT
logging.info(f"Service URL and Port: {self.urlPort}")

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


@app.route("/getTeams")
def getTeams():
  
  url = f"http://{self.urlPort}/db/get/teams"

  resp = http.request('GET', url)
  print(resp.status)
  print(resp.json())

  json_html = resp.json()

  print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("teams.html", len = len(json_html), json_html = json_html) 
   
  app.run(use_reloader = True, debug = True) 

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)