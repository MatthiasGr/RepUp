from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class AchievementReg(Base):
    userID = Column(Integer, ForeignKey('points.userID'), primary_key=True)
    achievementID = Column(Integer, ForeignKey('achievements.achievementID'), primary_key=True)
    time_of_achievement = Column(DateTime, default=datetime.utcnow)

    __tablename__ = 'achievementReg'

    def __repr__(self):
        return f'<Achievement {self.achievementID} achieved by {self.userID}>'


class PointsReg(Base):
    userID = Column(Integer, primary_key=True)
    points = Column(Integer)

    achievements = relationship('AchievementReg', backref='user')
    pendings = relationship('WaitingReg', backref='pending_issue')

    __tablename__ = 'pointsReg'

    def __repr__(self):
        return f'<User {self.userID}>'


class WaitingReg(Base):
    userID = Column(Integer, ForeignKey('pointsReg.userID'), primary_key=True)
    pending_issueID = Column(Integer)
    time_of_pending = Column(DateTime, default=datetime.utcnow)

    __tablename__ = 'pendingIssues'

    def __repr__(self):
        return f'<Pending issues of {self.userID}>'


class AchievementCatalog(Base):
    achievementID = Column(Integer, primary_key=True)
    # logo TODO

    achieved = relationship('AchievementReg', backref='achievement')

    __tablename__ = 'achievements'

    def __repr__(self):
        return f'<Achievement {self.achievementID}>'

