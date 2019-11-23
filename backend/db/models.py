from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AchievementReg(Base):
    userID = Column(Integer, ForeignKey('points.userID'), primary_key=True)
    achievementID = Column(Integer, ForeignKey('achievements.achievementID'), primary_key=True)
    time_of_achievement = Column(DateTime)

    __tablename__ = 'achievementReg'

    def __repr__(self):
        return f'<Achievement {self.achievementID} achieved by {self.userID}>'


class PointsReg(Base):
    userID = Column(Integer, primary_key=True)
    points = Column(Integer)

    __tablename__ = 'points'

    def __repr__(self):
        return f'<User {self.userID}>'


class WaitingReg(Base):
    userID = Column(Integer, ForeignKey('points.userID'), primary_key=True)
    pending_issueID = Column(Integer)
    time_of_pending = Column(DateTime)

    __tablename__ = 'pendingIssues'

    def __repr__(self):
        return f'<Pending issues of {self.userID}>'


class AchievementCatalog(Base):
    achievementID = Column(Integer, primary_key=True)
    # logo TODO

    __tablename__ = 'achievements'

    def __repr__(self):
        return f'<Achievement {self.achievementID}>'

