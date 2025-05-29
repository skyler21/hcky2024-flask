import datetime
import subprocess

today = datetime.date.today()
print(today)


days = datetime.timedelta(days=1)
print('One day  :', days)

yesterday = today - days
print('Yesterday:', yesterday)

count = 0
while (count < 110):
    count = count + 1
    URL = "http://localhost:8085/api/update/game/updateDate=" + str(yesterday)
    days = datetime.timedelta(days=count)
    print("URL is " + URL)
    yesterday = today - days


    # The command you would type in the terminal
    command = ["curl", URL]

    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output and error message (if any)
    output = result.stdout
    error = result.stderr

    # Check if it was successful
    if result.returncode == 0:
        print("Success:")
        print(output)
    else:
        print("Error:")
        print(error)

