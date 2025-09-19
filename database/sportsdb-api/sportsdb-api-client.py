import requests
import datetime
import sys
sys.path.append("/home/frank/surgesix/database")
from dbtables import Games
from db import SessionLocal

BASE_URL = "https://www.thesportsdb.com/api/v1/json/123/eventsseason.php?id=4391&s=2025"

def pulldata():
    response = requests.get(f"{BASE_URL}")
    print(response)
    data = response.json()

    cleanEvents = []
    for event in data.get("events", []):
        cleanEvents.append({
            "id": event["idEvent"],
            "game": event["strEventAlternate"],
            "season": event["strSeason"],
            "team1": event["strHomeTeam"],
            "team2": event["strAwayTeam"],
            "score1": event["intHomeScore"],
            "score2": event["intAwayScore"],
            "date": event["dateEvent"]
            })

    for ev in cleanEvents:
        print("\n\n\nThis is the start of a new event\n\n\n")
        print(ev)

    session = SessionLocal()

    for e in cleanEvents:
        existing = session.query(Games).filter_by(id=ev["id"]).first()
        if existing:
            continue
        else:
            game = Games(
                id=e["id"],
                game=e["game"],
                season=e["season"],
                team1=e["team1"],
                team2=e["team2"],
                finalscore1=e.get("score1"),
                finalscore2=e.get("score2"),
                date=e["date"]
            )
            session.add(game)
            session.commit()

    session.close()

pulldata()
