from sqlalchemy import Column, Integer, DateTime, VARCHAR
from datetime import datetime
from db import db


class PointsReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    points = Column(Integer)

    __tablename__ = 'pointsReg'

    def __repr__(self):
        return f'<User {self.userID}>'


class AchievementReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    achievementID = Column(Integer, primary_key=True)
    time_of_achievement = Column(DateTime, default=datetime.utcnow)

    __tablename__ = 'achievementReg'

    def __repr__(self):
        return f'<Achievement {self.achievementID} achieved by {self.userID}>'


class PendingReg(db.Model):
    userID = Column(VARCHAR(length=32), primary_key=True)
    pending_issueID = Column(VARCHAR(length=32))
    time_of_pending = Column(DateTime, default=datetime.utcnow)

    __tablename__ = 'pendingIssues'

    def __repr__(self):
        return f'<Pending issues of {self.userID}>'


class AchievementCatalog(db.Model):
    achievementID = Column(Integer, primary_key=True)
    # logo TODO

    __tablename__ = 'achievements'

    def __repr__(self):
        return f'<Achievement {self.achievementID}>'

