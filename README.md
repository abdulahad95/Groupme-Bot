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
