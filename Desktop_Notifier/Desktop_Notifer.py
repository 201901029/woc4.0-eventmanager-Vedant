#First write your routine inside the Daily Routine file and then execute this program
#This program will notify you according to your routine


def check(s1,s2):   #Checking whether current time is less than or equal to the time of the task scheduled 
        str1=s1.split(':')  #s1 is current time
        str2=s2.split(':')  #s2 is the time of scheduled task
        index=0
        while index<len(str1):
                if(int(str1[index])>int(str2[index])):
                        return False;
                elif(int(str1[index])<int(str2[index])):
                        return True;
                else:
                        index=index+1
        return True

import time
from plyer import notification    

f1=open('Desktop_Notifier/Daily Routine.txt','r')  #Open the daily routine file in read mode
x=1
flag=0
for line in f1:                   
        str=line.split(' ')  
        print(str)
        flag=0
        count=0
        while(x==1):
                temp=time.strftime('%H:%M:%S')  #Convert the time into string format 
                t1=check(temp,str[0])
                if(t1==False):                  #If time is passed notification will not generate
                        flag=1;
                        break;
                if temp==str[0]:               #If time is arrived loop will break and notification will generated
                        break;
                else:
                        continue;
        if(flag==1):                            #If time is passed for the task go to next task
                continue
        notification.notify(                    #Generate Notification
            title = "please do this",
            message=line ,
            # displaying time
            timeout=10
        )
