from flask import Flask, request, session
from you_track.auth import YouTrackAuthorization
import you_track.api as yt
import json
import db.helper as helper
import os.path as path
import os
from db.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
#dbm.db = db


app.secret_key = b'ZsaRkUmTSumtrk94gQ4edHf5AFYEWR4n'


# API Routes
@app.route("/api/user/login", methods=["POST"])
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
    return json.dumps("OK")


@app.route("/api/leaderboard", methods=["GET"])
def leaderboard():
    auth = YouTrackAuthorization(session["token"])
    #TODO: Update database entries
    #Get leaders from database
    entries = helper.Query.getUserPoints()
    entries = entries.sort(lambda x: x[1])[:10]
    def mapper(ent):
        data = yt.User.info(auth, ent[0])
        return {"name": data["name"], "score": ent[1]}
    entries = list(map(mapper, entries))
    return json.dumps(entries)


if __name__ == '__main__':
    app.run(port=1234)
