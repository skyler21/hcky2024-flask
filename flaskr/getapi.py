import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.exceptions import abort
import urllib3

bp = Blueprint('getapi', __name__)

print(urllib3.__version__)
http = urllib3.PoolManager()

@bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
       # form has been submitted, process data 
       rtnDate = request.form['dateVal']  
       return redirect(url_for("getGamesForDate"))
    else: 
       return render_template('index.html')

@bp.route("/getTeams")
def getTeams():
  
  url = 'http://localhost:8085/db/get/teams'

  resp = http.request('GET', url)
  print(resp.status)
  print(resp.json())

  json_html = resp.json()

  print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("teams.html", len = len(json_html), json_html = json_html) 
   
  # if __name__ == '__main__': 
  # running app 

  app.run(use_reloader = True, debug = True) 


@bp.route("/getGamesForDate")
def getGames(rtnDate):
  
  url = 'http://localhost:8085/db/get/games/{{ rtnDate }}'

  resp = http.request('GET', url)
  print(resp.status)
  print(resp.json())

  json_html = resp.json()

  print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("games.html", len = len(json_html), json_html = json_html) 
   
  # if __name__ == '__main__': 
  # running app 

  app.run(use_reloader = True, debug = True) 

