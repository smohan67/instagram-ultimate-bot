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
            sleep(5)
            print('success')
            break
        except:
            print('Failled. Invalid credentials or issue downloading the chromedriver.')
            continue




print('')
print("Welcome to the instagram bot!")
print('This has many features')






def get_num():
    while True:
        try:
            choice=int(input('Enter the number for the command you want to do: '))
            if choice<1 or choice>4:
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
    print('3. You can download all of someones posts(NOTE: Cant download videos and only downloads the 1st pictures of each post and takes a while if the account has a lot of posts)')
    print('4. Quit')
    print('')
    print('')

    choice=get_num()
    if choice==1:
        m=input('Do u want to send a message to each one of your unfollowers?(type yes or Yes if you want that)')
        if m=='yes' or m=='Yes':
            try:
                print('Gonna send a message')
                b=Bot(username,password)
                b.get_unfollowers(send_message=True)
            except:
                print('Error')
        else:
            try:
                b=Bot(username,password)
                b.get_unfollowers()
            except:
                print('Did you close Chrome?')
        continue
    elif choice==2:
        user=input('Enter the username of the person who you want to send a message: ')
        message=input('Enter the message you want to send:')
        spam=input('Do you want to spam them?(yes/no)')
        if spam=='Yes' or 'yes':
            spam_number=int(input('How many times do you want to spam them?(Max is 100)'))
            if spam_number>100:
                print('Deafalting to 100 times')
                spam_number=100
                print('Spamming +\''+user+' '+str(spam_number)+' times with the meassage \"'+message+'\"')
            b=Bot(username,password)
            b.send_message(user,message,spam_number)
            print('Messages sent!')
        else:
            b=Bot(username,password)
            b.send_message(user,message)
            print('Message sent!')
        continue
            
    elif choice==3:
        account=input('Which account do u want to download?')
        b=Bot(username,password)
        b.download_all_users_posts(account)
        continue
    else:
        try:
            b.driver.close()
            break
        except:
            break
    
