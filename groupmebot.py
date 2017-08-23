import sys
from time import sleep, strftime

try:
        from bs4 import BeautifulSoup
        import requests
except Exception as e:
	sys.exit('Error: %s' % e)

def getwebsite(link):
        response = requests.get(link)
        if response.status_code != 200:
                sys.exit()
        html = response.text
        return html
        

def getMaghribinfo():
        link = 'http://www.salatimes.com/index/index/lat/38.02632348914444/long/-78.51293563842773/method/2/ccode//region//q/UVA#.WTXdzWjytPY'
        html = getwebsite(link)
        soup = BeautifulSoup(html, "html.parser")
        #print (soup.prettify())
        time = soup.find("tr", class_="info").contents[6].contents
        time = (str(time))
        time = (time[2:7])
        text = 'Maghrib today is at ' + time
        return text
        #print (text)

def post():
        values = {'bot_id' : '132b154147f3c7edb6e02ba5b7', 'text' : getMaghribinfo()}
        requests.post('https://api.groupme.com/v3/bots/post', params = values)


post()       

#while 1:
        #hour = strftime('%H')

        #if hour == '17':
                #post()

        #sleep(7200)           



---------------------------------------
Command I'm running on terminal to create a bot in a certain group:
curl -X POST -d '{"bot": { "name": "Manhoos", "group_id": "30838218"}}' -H 'Content-Type: application/json' https:/api.groupme.com/v3/bots?token=MY_TOKEN  

^you can run this command to create a bot in a group. Thats's what I did. I think.

GroupMe API is confusing indeed:

Another command that I think can be used to run to create a bot:
curl -X POST https://api.groupme.com/v3/bots?token=yVm9KJMokULdzt4hmS0482y6w8T6Pg0HSV8BU76f&name='manhoos'&group_id='30838218'

Lo and behold, output of this 2nd command:
{"meta":{"code":"400","errors":["Missing/invalid bot parameters"]},"response":null}


When I switch the token, name, group_id around like this:
curl -X POST https://api.groupme.com/v3/bots?name='Manhoos'&group_id='30838218'&token=yVm9KJMokULdzt4hmS0482y6w8T6Pg0HSV8BU76f

Output:
First it says 
[1] 58911      <--- no idea what that means
[2] 58912      <--- no idea what this is either
then
{"response":null,"meta":{"code":401,"errors":["unauthorized"]}}



