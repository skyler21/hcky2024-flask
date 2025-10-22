import flask
from flask import Flask,render_template
import sys
import os
import logging
from flask import request
import http.client
import urllib3
import json
#import jsonify


logging.basicConfig(stream=sys.stdout, 
    format='%(asctime)s|%(levelname)s|%(thread)s|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG)

serviceName = 'localhost'
##serviceName = 'hockey2024app-hockey-service'
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
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("teams.html", len = len(json_html), json_html = json_html) 
   
@app.route("/getGames")
def getGames():
  
  url = f"http://{serviceName}:{servicePort}/db/get/games"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("games.html", len = len(json_html), json_html = json_html) 
  
@app.route("/findGames", methods=["GET","POST"] )
def findGames():

  gmSeason = request.args['gameSeason']
  gmType = request.args['gameType']
  gmTeam = request.args['gameTeam']
  gmDate = request.args['gameDate']

  url = f"http://{serviceName}:{servicePort}/db/get/findGames?gameSeason={gmSeason}&gameType={gmType}&gameTeam={gmTeam}&gameDate={gmDate}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("games.html", len = len(json_html), json_html = json_html) 

  app.run(use_reloader = True, debug = True) 

@app.route("/getGamesMenu")
def getGamesMenu():
  
  # get list of game seasons   
  url = f"http://{serviceName}:{servicePort}/db/get/allGameSeasons"

  seasonsResp = https.request('GET', url)
  gameSeasons = json.loads(seasonsResp.data)

  print(gameSeasons)
  
  # get list of game types  
  url = f"http://{serviceName}:{servicePort}/db/get/allGameTypes"

  typesResp = https.request('GET', url)
  gameTypes = json.loads(typesResp.data)

  #print(gameTypes)

  # get list of game teams   
  url = f"http://{serviceName}:{servicePort}/db/get/allGameTeams"

  teamsResp = https.request('GET', url)
  gameTeams = json.loads(teamsResp.data)
  gameTeams.append('NONE')

  #print(gameTeams)
  
  
  return render_template("gamesMenu.html", gameSeasons=gameSeasons, gameTypes=gameTypes, gameTeams=gameTeams) 
  
  app.run(use_reloader = True, debug = True) 

@app.route("/getStandings")
def getStandings():
  
  url = f"http://{serviceName}:{servicePort}/db/get/standings"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("standings.html", len = len(json_html), json_html = json_html) 

@app.route("/getWinPercent")
def getWinPercent():
  
  url = f"http://{serviceName}:{servicePort}/db/get/winPercent"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("standings.html", len = len(json_html), json_html = json_html) 
        
@app.route("/getTeamsMenu")
def getTeamsMenu():
  
  # returning index.html and list 
  # and length of list to html page 
  return render_template("teamsMenu.html") 
  
  app.run(use_reloader = True, debug = True) 

@app.route("/getStandingsMenu")
def getStandingsMenu():
  
  # returning index.html and list 
  # and length of list to html page 
  return render_template("standingsMenu.html") 
  

@app.route("/getRostersMenu")
def getRostersMenu():
  
  # returning index.html and list 
  # and length of list to html page 
  return render_template("rostersMenu.html") 

@app.route("/getLoadUpdatesMenu")
def getLoadUpdatesMenu():
  
  # returning index.html and list 
  # and length of list to html page 
  return render_template("loadUpdatesMenu.html") 

@app.route("/getGoalies")
def getGoalies():
  
  url = f"http://{serviceName}:{servicePort}/db/get/goalieRoster"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("goaliesRoster.html", len = len(json_html), json_html = json_html) 

@app.route("/getForwards")
def getForwards():
  
  url = f"http://{serviceName}:{servicePort}/db/get/forwardRoster"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("forwardsRoster.html", len = len(json_html), json_html = json_html) 

@app.route("/getDefense")
def getDefense():
  
  url = f"http://{serviceName}:{servicePort}/db/get/defenseRoster"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))

  json_html = json.loads(resp.data)

  #print(json_html)

  # returning index.html and list 
  # and length of list to html page 
  return render_template("defenseRoster.html", len = len(json_html), json_html = json_html) 

@app.route('/getTeamRoster/<team_id>')
def getTeamRoster(team_id):
   # Get Team Name
  url = f"http://{serviceName}:{servicePort}/db/get/teamName/team={team_id}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  teamName = resp.data.decode('utf-8')

 # Get Standings details
  url = f"http://{serviceName}:{servicePort}/db/get/teamStanding/team={teamName}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  standings_html = json.loads(resp.data)


 # Get Goalie details
  url = f"http://{serviceName}:{servicePort}/db/get/teamGoalieRoster/team={team_id}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  goalies_html = json.loads(resp.data)

  # Get Defense details
  url = f"http://{serviceName}:{servicePort}/db/get/teamDefenseRoster/team={team_id}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  defenses_html = json.loads(resp.data)
  
  # Get Forward details
  url = f"http://{serviceName}:{servicePort}/db/get/teamForwardRoster/team={team_id}"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  forwards_html = json.loads(resp.data)
  
  # Implement this function
  return render_template('teamRoster.html', teamName=teamName, standings=standings_html, goalies_len=len(goalies_html),goalies=goalies_html, defenses_len=len(defenses_html), defenses=defenses_html, forwards_len=len(forwards_html), forwards=forwards_html)

@app.route('/getDateRoster', methods=["GET","POST"])
def getDateRoster():
    gmDate = request.args['gameDate']

    # Get Team List for Date
    url = f"http://{serviceName}:{servicePort}/db/get/teamListByDate?gameDate={gmDate}"

    resp = https.request('GET', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    #print("Response headers = " + str(resp.headers))
    
    teamResp = json.loads(resp.data)
    if not teamResp:
        return "No teams found for this date"

     # Convert list to comma-separated string for API call
    teamList = ','.join(str(team) for team in teamResp)
     
    # Get Goalie details using the formatted team list
    url = f"http://{serviceName}:{servicePort}/db/get/GoaliesByTeamList/teamList={teamList}"

    resp = https.request('GET', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    #print("Response headers = " + str(resp.headers))
    
    goalies_html = json.loads(resp.data)

    # Get Defense details
    url = f"http://{serviceName}:{servicePort}/db/get/DefenseByTeamList/teamList={teamList}"

    resp = https.request('GET', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    #print("Response headers = " + str(resp.headers))
    
    defenses_html = json.loads(resp.data)
    
    # Get Forward details
    url = f"http://{serviceName}:{servicePort}/db/get/ForwardsByTeamList/teamList={teamList}"

    resp = https.request('GET', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    #print("Response headers = " + str(resp.headers))
    forwards_html = json.loads(resp.data)
    
    # Implement this function
    return render_template('dateRoster.html', gmDate=gmDate, goalies_len=len(goalies_html),goalies=goalies_html, defenses_len=len(defenses_html), defenses=defenses_html, forwards_len=len(forwards_html), forwards=forwards_html)

@app.route("/loadAllTeams")
def loadAllTeams():

  url = f"http://{serviceName}:{servicePort}/api/load/teams"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  resp_message = resp.data.decode('utf-8')

  #print(resp_message)
  ## display response message on curret html page
  message = f"Loaded {resp_message} from API"
  #print(message)

  # returning index.html and list
  # and length of list to html page
  return render_template("loadUpdatesMenu.html", message=message)

@app.route("/loadAllGames")
def loadAllGames():

  url = f"http://{serviceName}:{servicePort}/api/load/games"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  resp_message = resp.data.decode('utf-8')

  #print(resp_message)
  ## display response message on curret html page
  message = f"Loaded {resp_message} from API"
  #print(message)

  # returning index.html and list
  # and length of list to html page
  return render_template("loadUpdatesMenu.html", message=message)

@app.route("/updateDayRosters", methods=["POST"])
def updateDayRosters():
    gmDate = request.form.get('gameDate')  # Changed from request.args to request.form
    if not gmDate:
        return render_template("loadUpdatesMenu.html", 
                            message="Error: Date is required")

    # load Roster for gmDate
    url = f"http://{serviceName}:{servicePort}/api/load/roster/date={gmDate}"

    resp = https.request('POST', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    
    resp_message = resp.data.decode('utf-8')
    message = f"Loaded {resp_message} from API"
    
    return render_template("loadUpdatesMenu.html", message=message)

@app.route("/updateDayGames", methods=["POST"])
def updateDayGames():
    gmDate = request.form.get('gameDate')  # Changed from request.form[] to request.form.get()
    if not gmDate:
        return render_template("loadUpdatesMenu.html", 
                            message="Error: Date is required")
 
    # update Game for gmDate
    url = f"http://{serviceName}:{servicePort}/api/update/game/updateDate={gmDate}"

    resp = https.request('POST', url)
    #print("Response Status = " + str(resp.status))
    #print("Response DATA = " + str(resp.data))
    
    resp_message = resp.data.decode('utf-8')
    message = f"Loaded {resp_message} from API"

    return render_template("loadUpdatesMenu.html", message=message)

@app.route("/loadStandings")
def loadStandings():

  url = f"http://{serviceName}:{servicePort}/api/load/standings"

  resp = https.request('GET', url)
  #print("Response Status = " + str(resp.status))
  #print("Response DATA = " + str(resp.data))
  #print("Response headers = " + str(resp.headers))
  
  resp_message = resp.data.decode('utf-8')

  #print(resp_message)
  ## display response message on curret html page
  message = f"Loaded {resp_message} from API"
  #print(message)

  # returning index.html and list
  # and length of list to html page
  return render_template("loadUpdatesMenu.html", message=message)

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
