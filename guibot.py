from InstagramAPI import *
from tkinter import *
import tkinter


class LogIn:

    def log():

        global username
        global password

        followers = []  # Dictionary of people that follow you
        followings = []  # Dictionary of people that you follow

        nonFollowersIDs = []  # Dictionary of people that do not follow me
        nonFollowersNames = []  # Dictionary of people that do not follow me

        nonFollowingNames = []  # Dictionary of people that I do not follow
        nonFollowingIDs = []  # Dictionary of people that I do not follow

        # Generates a list of people that are following me
        def selfFollowers():

            temp = session.getTotalSelfFollowers()

            for x in temp:
                user = {'username': x['username'], 'id': x['pk']}
                followers.append(user)

        # Generates a list of people I am following
        def selfFollowing():

            temp = session.getTotalSelfFollowings()

            for x in temp:
                user = {'username': x['username'], 'id': x['pk']}
                followings.append(user)

        # Generates a list of people who are not following me back
        def notFollowers():
            for x in followings:
                found = False
                for y in followers:
                    if x['id'] == y['id']:
                        found = True
                        break
                if not found:
                    nonFollowersIDs.append(x['id'])

            for x in followings:
                found = False
                for y in followers:
                    if x['username'] == y['username']:
                        found = True
                        break
                if not found:
                    nonFollowersNames.append(x['username'])

        # Generates a list of people that I am not following back
        def notFollowing():
            for x in followers:
                found = False
                for y in followings:
                    if x['id'] == y['id']:
                        found = True
                        break
                if not found:
                    nonFollowingIDs.append(x['id'])

            for x in followers:
                found = False
                for y in followings:
                    if x['username'] == y['username']:
                        found = True
                        break
                if not found:
                    nonFollowingNames.append(x['username'])

        # Unfollows people who do not follow me back (max 100)
        def unfollowNotFollowingBack():
            counter = 0
            for x in nonFollowersIDs:
                session.unfollow(x)
                counter += 1
                if counter == 100:
                    break

            # Reset everything
            followers.clear()
            followings.clear()
            nonFollowersIDs.clear()
            nonFollowersNames.clear()
            selfFollowers()
            selfFollowing()
            notFollowers()

        # Follows people I am not following back (max 100)
        def followNotFollowingBack():
            counter = 0
            for x in nonFollowingIDs:
                session.follow(x)
                counter += 1
                if counter == 100:
                    break

            # Reset everything
            followers.clear()
            followings.clear()
            nonFollowersIDs.clear()
            nonFollowersNames.clear()
            selfFollowers()
            selfFollowing()
            notFollowers()

        username = input("What is your username?\n")
        password = input("What is your password?\n")

        session = InstagramAPI(username, password)
        session.login()

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
                exit()

    window = tkinter.Tk()
    window.title("Login")
    window.configure(background = "white")

    Label(window, text = "User Name").grid(row=0)
    Label(window, text = "Password").grid(row=1)

    e1 = Entry(window)
    e2 = Entry(window)

    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)

    login = Button(window, text = "Log In", command = log)
    forgot = Button(window, text = "Forgot Password")

    login.grid(row = 3, column = 0, sticky = "W", pady =  8)
    forgot.grid(row = 3, column = 1, sticky= "W", pady =  8)

    window.mainloop()