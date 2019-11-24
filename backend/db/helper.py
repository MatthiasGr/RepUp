from db.models import *
from sqlalchemy import func

#HACK
import sys
sys.path.append("..")
from main import db


class Insert:
    @staticmethod
    def existing_user(userID):
        return PointsReg.query.filter(PointsReg.userID == userID).first()

    @staticmethod
    def existing_achievement(achievementID):
        return AchievementCatalog.query.filter(AchievementCatalog.achievementID == achievementID).first()

    @staticmethod
    def addDB(object):
        db.session.add(object)
        db.session.commit()

    @staticmethod
    def newUser(userID):
        if Insert.existing_user(userID):
            return f'User {userID} already exists'
        new_user = PointsReg(userID=userID, points=0)
        new_user_counter = Counter(userID=userID, number_issues=0)
        Insert.addDB(new_user)
        Insert.addDB(new_user_counter)
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
            Insert.newUser(userID)
            #return f'User {userID} does not exist'
        existing_issue = PendingReg.query.filter(PendingReg.userID == userID).filter(PendingReg.pending_issueID == issueID).first()
        if existing_issue:
            print(f'Issue {issueID} already pending for User {userID}')
            return f'Issue {issueID} already pending for User {userID}'
        new_issue = PendingReg(userID=userID, pending_issueID=issueID, time_of_pending=time_of_pending)
        Insert.addDB(new_issue)
        print(f'Issue {issueID} successfully added to User {userID}')
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
        user = PointsReg.query.filter(PointsReg.userID == userID).first()
        user.points += points
        db.session.commit()
        print(f'Update Points for {userID} successful')

    @staticmethod
    def get_pending(userID, issueID):
        if not Insert.existing_user(userID):
            print(f'User {userID} does not exist')
            return None
        if not Update.existing_issue(issueID):
            print(f'Issue {issueID} does not exist for User {userID}')
            return None
        pending_issue = PendingReg.query.filter(PendingReg.userID == userID).filter(PendingReg.pending_issueID == issueID).first()
        return pending_issue

    @staticmethod
    def get_pending(issueID):
        if not Update.existing_issue(issueID):
            print(f'Issue {issueID} does not exist')
            return None
        pending_issue = PendingReg.query.filter(PendingReg.pending_issueID == issueID).first()
        return pending_issue

    @staticmethod
    def remove_pending(pendingIssue):
        db.session.delete(pendingIssue)
        db.session.commit()
        print('Deletion of pending successful')

    @staticmethod
    def remove_user(userID):
        if not Insert.existing_user(userID):
            return f'User {userID} does not exist'
        db.session.delete(PointsReg.query.filter(PointsReg.userID==userID).first())
        #db.session.delete(AchievementReg.query.filter(AchievementReg.userID==userID).first())
        db.session.commit()
        print('Deletion of user successful')

    @staticmethod
    def close_pending(issueID, ending_time, prio):
        pending = Update.get_pending(issueID=issueID)
        #print(pending.convert())
        if pending is not None:
            # difference in minutes
            diff = ending_time - pending.time_of_pending / 60000.0

            points = Update.point_gen(diff, prio)
            Update.updatePoints(pending.userID, points)
            Update.inc_user_issue(pending.userID)
            Update.remove_pending(pending)
            print(f'Successful closing')
        else:
            print(f'No pending found')

    @staticmethod
    def point_gen(number, prio):
        base_points = 2268 / (number ** (1 / float(5))) + prio
        return base_points if base_points < 3600 * 10 else base_points + 500

    @staticmethod
    def inc_user_issue(userID):
        if not Insert.existing_user(userID):
            return f'User {userID} does not exist'
        user = Counter.query.filter(PointsReg.userID == userID).first()
        user.number_issues += 1
        db.session.commit()
        print(f'Update Points for {userID} successful')


class Query:
    @staticmethod
    def getUserPoints():
        basic_users = PointsReg.query.all()
        return list(map(lambda x: x.convert(), basic_users))

    @staticmethod
    def getPendings():
        basic_pendings = PendingReg.query.all()
        return list(map(lambda x: x.convert(), basic_pendings))

    @staticmethod
    def getCounters():
        basic_counters = Counter.query.all()
        return list(map(lambda x: x.convert(), basic_counters))

    @staticmethod
    def showDB():
        #print(PointsReg.query.all())
        #print(PendingReg.query.all())
        print(Query.getUserPoints())
        print(Query.getPendings())
        print(Query.getCounters())

    @staticmethod
    def isPending(issueID):
        if not Update.existing_issue(issueID):
            print(f'Issue {issueID} does not exist')
            return False
        return True


class Delete:
    @staticmethod
    def clearDB():
        PendingReg.query.delete()
        AchievementReg.query.delete()
        AchievementCatalog.query.delete()
        PointsReg.query.delete()
        Counter.query.delete()
        db.session.commit()

