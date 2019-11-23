from db.models import *
from sqlalchemy import func
from db import db


class Insert:
    @staticmethod
    def existing_user(userID):
        return PointsReg.query.filter(PointsReg.userID == userID).first()

    @staticmethod
    def existing_achievement(achievementID):
        return AchievementCatalog.query.filter(AchievementCatalog.achievementID == achievementID)

    @staticmethod
    def addDB(object):
        db.session.add(object)
        db.session.commit()

    @staticmethod
    def newUser(userID):
        if Insert.existing_user(userID):
            return f'User {userID} already exists'
        new_user = PointsReg(userID=userID, points=0)
        Insert.addDB(new_user)
        return f'User {userID} successfully created'

    @staticmethod
    def newAchievement(userID, achievementID, time_of_achievement):
        if not Insert.existing_user(userID):
            return f'User {userID} does not exist'
        if not Insert.existing_achievement(achievementID):
            return f'Achievement {achievementID} does not exist'
        existing_achievement = AchievementReg.query.filter(AchievementReg.userID == userID
                                                           and AchievementReg.achievementID == achievementID).first()
        if existing_achievement:
            return f'User {userID} already achieved achievement {achievementID}'
        new_achievement = AchievementReg(userID=userID, achievementID=achievementID, time_of_achievement=time_of_achievement)
        Insert.addDB(new_achievement)
        return f'Achievement {achievementID} successfully set for User {userID}'

    @staticmethod
    def newPendingIssue(userID, issueID, time_of_pending):
        if not Insert.existing_user(userID):
            return f'User {userID} does not exist'
        existing_issue = PendingReg.query.filter(PendingReg.userID == userID and PendingReg.pending_issueID == issueID)
        if existing_issue:
            return f'Issue {issueID} already pending for User {userID}'
        new_issue = PendingReg(userID=userID, pending_issueID=issueID, time_of_pending=time_of_pending)
        Insert.addDB(new_issue)
        return f'Issue {issueID} successfully added to User {userID}'

    @staticmethod
    def newAchievementCat(achievementID):
        if Insert.existing_achievement(achievementID):
            return f'Achievement {achievementID} already exists'
        new_achievement = AchievementCatalog(achievementID=achievementID)
        Insert.addDB(new_achievement)
        return f'Achievement {achievementID} successfully set'


class Update:
    @staticmethod
    def existing_issue(issueID):
        return PendingReg.query.filter(PendingReg.pending_issueID == issueID).first()

    @staticmethod
    def updatePoints(userID, points):
        if not Insert.existing_user(userID):
            return f'User {userID} does not exist'
        user = PointsReg.query.filter(userID == userID).first()
        user.points = points
        db.session.commit()

    @staticmethod
    def get_pending(userID, issueID):
        if not Insert.existing_user():
            return f'User {userID} does not exist'
        if not Update.existing_issue(issueID):
            return f'Issue {issueID} does not exist for User {userID}'
        pending_issue = PendingReg.query.filter(PendingReg.userID==userID, PendingReg.pending_issueID==issueID).first()
        return pending_issue

    @staticmethod
    def remove_pending(pendingIssue):
        db.session.delete(pendingIssue)
        db.session.commit()

    @staticmethod
    def remove_user(userID):
        if not Insert.existing_user():
            return f'User {userID} does not exist'
        db.session.delete(PointsReg.query.filter(PointsReg.userID==userID).first())
        db.session.delete(AchievementReg.query.filter(AchievementReg.userID==userID).first())
        db.session.commit()


class Query:
    @staticmethod
    def getUserPoints():
        basic_users = PointsReg.query.all()
        return list(map(lambda x : x.convert(), basic_users))