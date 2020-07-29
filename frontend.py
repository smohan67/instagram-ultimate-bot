from bot import *
from time import sleep


while True:
    username=input('Enter your username:')
    password=input('Enter your password:')
    confirm=input('Your username is '+username+' and your password is '+password+'. Enter No if this isnt true?')
    if confirm=='no' or confirm=='No':
        continue
    else:
        print('This will login to test if your account credentials work')
        
        try:
            b=Bot(username,password)
            b.go_to_others_profile(b.username)
            print('Testing in progress...Dont close the browser')
            sleep(5)
            b.driver.close()
            print('success')
            break
        except:
            print('Failled. Invalid credentials or you closed the browser')
            try:
                b.driver.close()
            except:
                pass
            continue




print('')
print("Welcome to the instagram bot!")
print('This has many features')






def get_num():
    while True:
        try:
            choice=int(input('Enter the number for the command you want to do: '))
            if choice<1 or choice>5:
                print('Not a valid choice')
            else:
                return choice
                break
        except:
            print('Not a valid choice')
            continue


while True:
    print('1. You can get the people that dont follow you back(NOTE: if you have a lot of followers, this might take 5-15 minutes)')
    print('2. You can send someone a message')
    print('3. You can follow or unfollow someone. The bot will base it on if your following or unfollowing them')
    print('4. You can download all of someones posts(NOTE: Cant download videos and only downloads the 1st pictures of each post and takes a while if the account has a lot of posts and u need to create a folder name (s) in the same directory)')
    print('5. Quit')
    print('')
    print('')

    choice=get_num()
    if choice==1:
        m=input('Do u want to send a message to each one of your unfollowers?(type yes or Yes if you want that)')
        if m=='yes' or m=='Yes':
            try:
                message=input('What message do u want to send to all the people that dont follow you back?')
                print('Gonna send a message')
                b=Bot(username,password)
                b.get_unfollowers(send_message=True,message=message)
                b.driver.close()
                continue
            except:
                print('Did you close Chrome?')
                continue
        else:
            try:
                b=Bot(username,password)
                b.get_unfollowers()
                b.driver.close()
            except:
                print('Did you close Chrome?')
                continue
    if choice==2:
        user=input('Enter the username of the person who you want to send a message: ')
        message=input('Enter the message you want to send:')
        try:
            b=Bot(username,password)
            b.send_message(user,message)
            print('Message sent!')
            b.driver.close()
            continue
        except:
            print('Message not sent. Please check your spelling of that name or you might have closed chrome.')
            try:
                b.driver.close()
                continue
            except:
                continue
    if choice==3:
        user=input('Who do u want to follow/unfollow? ')
        try:
            b=Bot(username,password)
            b.unfollow_or_follow_someone(user)
            print('Success')
            b.driver.close()
            continue
        except:
            print('Invalid user or you closed chrome')
            try:
                b.driver.close()
                continue
            except:
                continue
    if choice==4:
        account=input('Which account do u want to download?')
        try:
            b=Bot(username,password)
            b.download_all_users_posts(b.driver,account)
            b.driver.close()
            continue
        except:
            print('Invalid user or you closed chrome')
            try:
                b.driver.close()
                continue
            except:
                continue

    if choice==5:
        print('Thank you for using our service')
        break
