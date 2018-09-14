from InstagramAPI import *


class Bot:

    followers = []  # Dictionary of people that follow you
    followings = []  # Dictionary of people that you follow
    followersID = []  # List of follower IDs
    followingsID = []  # List of followings IDs
    usersToFollow = []  # Queue of who to follow

    nonFollowersIDs = []  # Dictionary of people that do not follow me
    nonFollowersNames = []  # Dictionary of people that do not follow me

    nonFollowingNames = []  # Dictionary of people that I do not follow
    nonFollowingIDs = []  # Dictionary of people that I do not follow

    def __init__(self):
        self.username = input("What is your username?\n")
        self.password = input("What is your password?\n")
        self.session = InstagramAPI(self.username, self.password)
        self.session.login()

    # Generates a list of people that are following me
    def selfFollowers(self):

        temp = self.session.getTotalSelfFollowers()

        for x in temp:
            user = {'username': x['username'], 'id': x['pk']}
            self.followers.append(user)
            self.followersID.append(x['pk'])

    # Generates a list of people I am following
    def selfFollowing(self):

        temp = self.session.getTotalSelfFollowings()

        for x in temp:
            user = {'username': x['username'], 'id': x['pk']}
            self.followings.append(user)
            self.followingsID.append(x['pk'])

    # Generates a list of people who are not following me back
    def notFollowers(self):
        for x in self.followings:
            found = False
            for y in self.followers:
                if x['id'] == y['id']:
                    found = True
                    break
            if not found:
                self.nonFollowersIDs.append(x['id'])

        for x in self.followings:
            found = False
            for y in self.followers:
                if x['username'] == y['username']:
                    found = True
                    break
            if not found:
                self.nonFollowersNames.append(x['username'])

    # Generates a list of people that I am not following back
    def notFollowing(self):
        for x in self.followers:
            found = False
            for y in self.followings:
                if x['id'] == y['id']:
                    found = True
                    break
            if not found:
                self.nonFollowingIDs.append(x['id'])

        for x in self.followers:
            found = False
            for y in self.followings:
                if x['username'] == y['username']:
                    found = True
                    break
            if not found:
                self.nonFollowingNames.append(x['username'])

    # Unfollows people who do not follow me back (max 100)
    def unfollowNotFollowingBack(self):
        counter = 0
        for x in self.nonFollowersIDs:
            self.session.unfollow(x)
            counter += 1
            if counter == 100:
                break

        # Reset everything
        self.followers.clear()
        self.followings.clear()
        self.nonFollowersIDs.clear()
        self.nonFollowersNames.clear()
        self.selfFollowers()
        self.selfFollowing()
        self.notFollowers()

    # Follows people I am not following back (max 100)
    def followNotFollowingBack(self):
        counter = 0
        for x in self.nonFollowingIDs:
            self.session.follow(x)
            counter += 1
            if counter == 100:
                break

        # Reset everything
        self.followers.clear()
        self.followings.clear()
        self.nonFollowersIDs.clear()
        self.nonFollowersNames.clear()
        self.selfFollowers()
        self.selfFollowing()
        self.notFollowers()

    def stealFollowers(self):
        otherFollowers = []  # List of people who the person you're looking at follows
        user_name = input("What user?")
        self.session.searchUsername(user_name)
        username_id = self.session.LastJson["user"]["pk"]
        print(username_id)
        temp = self.session.getTotalFollowers(username_id)
        for x in temp:
            otherFollowers.append(x['pk'])

        for x in otherFollowers:
            if x not in self.followingsID:
                self.usersToFollow.append(x)

    def gain(self):
        usersToRemove = []
        counter = 0
        for x in range(0, len(self.usersToFollow)):
            if self.usersToFollow[x] in self.followingsID:
                continue
            self.session.follow(self.usersToFollow[x])
            counter += 1
            usersToRemove.append(self.usersToFollow[x])
            if counter == 100:
                break
            print("UsersToFollow: " + str(len(self.usersToFollow)))
            print("Counter: " + str(counter))

        for x in usersToRemove:
            self.usersToFollow.remove(x)

    def start(self):
        # create = Bot(username2, password2)
        while True:
                print("\n----------------------------------------------------------------")
                print("|1. Follow all users who you are not following back.            |")
                print("|2. Unfollow all users who are not following you back.          |")
                print("|3. Steal and gain followers from your user of choice           |")
                print("|4. Exit                                                        |")
                print("-----------------------------------------------------------------")
                choice = int(input("What would you like to do?\n"))
                if choice == 1:
                    print("Following users who you are not following back")
                    self.followNotFollowingBack()
                elif choice == 2:
                    print("Unfollowing users who are not following you back")
                    self.selfFollowers()
                    self.selfFollowing()

                    self.unfollowNotFollowingBack()
                elif choice == 3:
                    print("Starting to copy followers")
                    self.selfFollowing()
                    self.selfFollowers()
                    self.stealFollowers()
                    self.gain()
                    print("Done copying followers")
                elif choice == 4:
                    self.session.logout()
                    break

# The bot running
'''
test = Bot("cashmoneycarl", "clvjr1666")
test = Bot("shadypingu_", "@AACwfgh6gm*3YJS")
test = Bot("shady.flow", "056357287042")
'''



