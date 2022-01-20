#This program stores the numbers of people along with their names and person can view the phone 
#numbers and if person enters some keyword then all the names corresponding to that 
#keyword can be obtained. Also person can view the entire contact list if he wants.

def search(s1,list):   #This function is used for checking all the names which are matching with the keyword
  index=0
  print("These are keywords which are matching\n")
  while index<len(list):
    temp=list[index].find(s1)
    if(temp!=-1):
      print(list[index])
    index=index+1

list=['Vedant','Vedantu','John','Johny','Rakesh','Raja']  
dict={'Vedant':{1:9408234965,2:4738352868},'Vedantu':{1:5246773882,2:9348204888},
'John':{1:2321740157,2:787521975},'Johny':{1:99135151601,2:9237296276},'Rakesh':{1:66829020861,2:7582952752},
'Raja':{1:5297138769,2:8918402158}}  #This nested dictionary used for storing multiple numbers of a person
x=1
print("Hello\n")
while(x==1):
  s=input("You Have three options:- Store , Retrieve and Exit. Please Select One.\n")
  if(s=="Exit"):
    break;
  elif(s=="Store"):
    name=input("Please Enter Your Name\n")
    temp=list.count(name)
    if(temp==0):         #If name is not present inside the list pass the name to the list and also create person's dictionary
      list.append(name)
      dict[name]={}
    t1=len(dict[name])
    t1=t1+1;
    no=int(input("Please enter your contact number\n"))
    dict[name][t1]=no    #Store the number inside the corresponding dictionary
    print("Your Contact is Successfully Stored\n")
  else:
    s=input("Do You want View the entire list: -Yes or No. Please Select One.\n")
    if(s=="Yes"):
      list.sort()   #Sort the list alphabetically
      index=0
      while index<len(list):  #This loop is used for printing the names and its corresponding numbers for all persons
        print(list[index])
        print(dict[list[index]])
        index=index+1
    else:
      s1=input("PLease Enter KeyWord\n")
      search(s1,list)    #Search names which have this keyword
      name=input("print enter your name\n")
      temp=len(dict[name])
      index=1
      while(index<=temp):  #Print the numbers of the person
        print(dict[name][index])
        index=index+1;