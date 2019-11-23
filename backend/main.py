from flask import Flask, request, session
from .you_track.auth import YouTrackAuthorization
import you_track.api as yt
import json

app = Flask(__name__)

# API Routes
@app.route("/api/user/login", methods="POST")
def login():
    token = request.json()["token"]
    auth = YouTrackAuthorization(token)
    # Test auth using our YouTrack api
    if yt.User.check_token(auth):
        session["token"] = token
        return json.dumps("OK")
    return json.dumps("Could not authenticate token")


@app.route("/api/user/logout", methods=["GET", "POST"])
def logout():
    session["token"] = None

@app.route("/api/leaderboard", methods="GET")
def leaderboard():
    #TODO: Update database entries
    #Get leaders from database
    pass
