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

    def __init__(self, username, password):
        # self.username = input("What is your username?\n")
        # self.password = input("What is your password?\n")
        self.username = username
        self.password = password
        self.session = InstagramAPI(username, password)
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

    '''
    # Getting followers
    list = session.getTotalSelfFollowers()
    
    for x in list:
        followerNames.append(x['username'])
        followerIDs.append(x['pk'])
    
    
    for x in followerNames:
        print(x)
    
    for x in followerIDs:
        print(x)
    
    # Getting followings
    
    list = session.getTotalSelfFollowings()
    
    for x in list:
        followingNames.append(x['username'])
        followingIDs.append(x['pk'])
    
    for x in followingNames:
        print(x)
    
    for x in followingIDs:
        print(x)
    '''

    '''
        while True:
                print("\n----------------------------------------------------------------")
                print("|1. Follow all users who you are not following back.            |")
                print("|2. Unfollow all users who are not following you back.          |")
                print("|3. Exit                                                        |")
                print("-----------------------------------------------------------------")
                choice = int(input("What would you like to do?\n"))
    
                if choice == 1:
                    followNotFollowingBack()
                    print("First")
                elif choice == 2:
                    unfollowNotFollowingBack()
                    print("Second")
                elif choice == 3:
                    print("Third")
                    session.logout()
                    break
    '''

# test = Bot("cashmoneycarl", "clvjr1666")
# test = Bot("shadypingu_", "@AACwfgh6gm*3YJS")


test = Bot("gmunsbe", "strive505")
test.selfFollowing()
test.selfFollowers()
test.stealFollowers()
print(test.usersToFollow)
print("-------------------------------------------")
test.gain()
print(test.usersToFollow)




