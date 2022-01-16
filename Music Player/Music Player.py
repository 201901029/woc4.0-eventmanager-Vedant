#This is the music player program using python which implements the basic functionalities
#like playing,pausing,resuming,stopping and changing volume.

from pygame import *  #pygame contains mixer which are used for playing song
import os               #os module is used for file operations
mixer.init()    #initialize the mixer
list=os.listdir("Music Player/music_files") #list contains list of all songs 
while(True):
  print("These are the songs present in your music player")
  index=0
  while index<len(list):   #This loop is used for printing names of all songs
    s1=list[index].split(".")
    print(s1[0])
    index=index+1
  
  s=input("Please Select One Song or Press E to exit the music Player\n ")
  if(s=="E"):
    break
  s1="Music Player/music_files/"+s+".mp3"    #This is the path of the song which is selected
  file_exists=os.path.exists(s1) #Checking whether song name entered is correct or not
  if(file_exists==False):
    print("Please Enter Correct Name") 
    continue
  mixer.music.load(s1)       #load the song
  mixer.music.set_volume(0.7)  #Set the Volume
  mixer.music.play()    #Play the Song
  while True:
    s=input("Please press p to pause the music\nr to resume the music\ns to stop the music\nv to change the volume\n")
    if s=="p":
      mixer.music.pause()       #Pause the Song
    elif s=='r':
      mixer.music.unpause()    #Resume the Song
    elif s=='v':                  
      temp=mixer.music.get_volume()   #Get the Current Volume   
      temp=temp*100
      t1=round(temp)
      print("Your Current Sound is ")
      print(t1)
      temp=int(input("Please Press between 1 to 100 for changing sound\n"))
      temp=temp/100
      mixer.music.set_volume(temp)  #Set the Volume
    else:
      mixer.music.stop()      #Stop the Music
      break

