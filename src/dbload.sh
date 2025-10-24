#!/bin/bash 
# create a shell script to run 3 curl commands
   # curl localhost:8085/api/load/standings  
   # curl localhost:8085/api/load/roster/date={gameDate}            
   # curl localhost:8085/api/update/game/updateDate={inputDate} 

echo "Load Standings."
curl hockey2025app-hockey-service:8085/api/load/standings
# delay for 5 seconds to allow standings to load
sleep 5
# calculate yesterday's date and use it as game date
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
INPUT_DATE=${YESTERDAY}
echo "Update Yesterday's Games."
curl hockey2025app-hockey-service:8085/api/update/game/updateDate=${INPUT_DATE}

# delay for 10 seconds to allow Games to load
sleep 10
#calculate today's date and use it as input date
TODAY=$(date +%Y-%m-%d)
GAME_DATE=${TODAY}
echo "Update Today's Rosters."
curl hockey2025app-hockey-service:8085/api/load/roster/date=${GAME_DATE}

# display message indicating completion
echo "Database load completed."

