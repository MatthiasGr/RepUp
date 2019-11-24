from sqlalchemy import Column, Integer, VARCHAR
from datetime import datetime

#HACK
import sys
sys.path.append("..")
from main import db


class PointsReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    points = Column(Integer)

    __tablename__ = 'pointsReg'

    def __repr__(self):
        return f'<User {self.userID}>'

    def convert(self):
        return self.userID, self.points


class AchievementReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    achievementID = Column(Integer, primary_key=True)
    time_of_achievement = Column(Integer)

    __tablename__ = 'achievementReg'

    def __repr__(self):
        return f'<Achievement {self.achievementID} achieved by {self.userID}>'


class PendingReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    pending_issueID = Column(VARCHAR(length=32), primary_key=True)
    time_of_pending = Column(Integer)

    __tablename__ = 'pendingIssues'

    def __repr__(self):
        return f'<Pending issues of {self.userID}>'

    def convert(self):
        return self.userID, self.pending_issueID, self.time_of_pending


class AchievementCatalog(db.Model):
    achievementID = Column(Integer, primary_key=True)
    # logo TODO

    __tablename__ = 'achievements'

    def __repr__(self):
        return f'<Achievement {self.achievementID}>'

