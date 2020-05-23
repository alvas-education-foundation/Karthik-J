print('****************************************************************************')
print('##############Enter Valid Username and Password###############\n')
print('****************************************************************************\n')

count=0
while count<3: #counts for 3 attempts
    
    username=input('Enter your username:')
    password=input('Enter your password:')
#print('****************************************************************************\n')

    if username=='Micheal'and password=='3$WT89x':
        #preinput data
        print('\nYou Have Sucessfully Loggedin!!\n ')
        break
    #Terminates if correct
    else:
        count+=1
        print('\ninvalid username/password\n')
        

        if count==3:
            # waits for 3 attemps after that prog terminates
            print('\nToo many attempts!!! Your account as been locked\n ')
print('****************************************************************************\n')
