import redis
from redis.commands.json.path import Path

client = redis.Redis(host='localhost', port=6379, db=0)

nfl_conferences = {
    'afc': {
        'north': [
            {
                "BAL": {
                    "full_name": "Baltimore Ravens",
                    "short_name": "Ravens",
                    "standings": {
                        "overall_wins": 0,
                        "overall_ties": 0,
                        "overall_losses": 0,
                        "division_wins": 0,
                        "division_ties": 0,
                        "division_losses": 0,
                        "conference_wins": 0,
                        "conference_ties": 0,
                        "conference_losses": 0
                    }
                }
            }, 
            {
                "CIN": {
                    "full_name": "Cincinatti Bengals",
                    "short_name": "Bengals"
               }
            }, "Cleveland Browns", "Pittsburgh Steelers"],
        'east' : ["Buffalo Bills", "Miami Dolphins", "New England Patriots", "New York Jets"]
    }
}


client.json().set('nfl_conferences', Path.root_path(), nfl_conferences)

result = client.json().get('nfl_conferences')
print(result)