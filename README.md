Base URL for all commands/requests:
https://api.groupme.com/v3


To check what bots you have in any/all groups;

GroupMe says to do:
GET /bots

Command you run:
curl https://api.groupme.com/v3/bots?token=MY_TOKEN


To create a bot:

GroupMe says to do:
POST /bots

bot[name] required
string
bot[group_id] required
string

Command you run:
curl -X POST -d '{"bot": { "name": "Manhoos", "group_id": "30838218"}}' -H 'Content-Type: application/json' https:/api.groupme.com/v3/bots?token=MY_TOKEN


To make bot post a message:

GroupMe says to do:
POST /bots/post

bot_id required
string
text required
string

Command you run:
curl -X POST -d '{"bot_id": "132b154147f3c7edb6e02ba5b7", "text": "Hello baby"}' -H 'Content-Type: application/json' https://api.groupme.com/v3/bots/post?token=yVm9KJMokULdzt4hmS0482y6w8T6Pg0HSV8BU76f

OR 

curl -X POST "https://api.groupme.com/v3/bots/post?bot_id=132b154147f3c7edb6e02ba5b7&text=Hello+baby"


