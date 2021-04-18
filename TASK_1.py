#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re
def vitvalid(email_id,vit_can):
    if re.match("^[a-z.]+[0-9]{4}@vitstudent\.ac\.in$",email_id):
        ans="YES"
        print("YES,THE USER BELONGS TO VIT UNIVERSITY")
        reg_no=input("ENTER VALID REG. NO.")
        while(re.match("^[1-2][0-9][A-Z]{3}[0-9]{4}$",reg_no)==None):
            print("INCORRECT")
            reg_no=input("ENTER VALID REG. NO.")
        phn_no=int(input("ENTER PHONE NUMBER"))
        while(len(str(phn_no))!=10):
            print("INCORRECT")
            phn_no=int(input("ENTER VALID PHONE NUMBER"))
        vit_can[email_id]=[email_id,ans,reg_no,phn_no]
        return
    else:
        ans="NO"
        print("NO,THE USER DOES NOT BELONGS TO VIT UNIVERSITY")
        phn_no=int(input("ENTER PHONE NUMBER"))
        while(len(str(phn_no))!=10):
            print("INCORRECT")
            phn_no=int(input("ENTER A VALID PHONE NUMBER"))
        vit_can[email_id]=[email_id,ans,"NULL",phn_no]
        return
        
print("************VIT CANDIDATES************\n")
print('''CHOOSE OPTION TO INSERT CANDIDATES/PERSONS\n
1.INSERT SPECIFIC NUMBER OF STUDENTS
2.INSERT A UNDEFINED NUMBER OF STUDENTS''')
print("\n")
x=int(input("GIVE YOUR CHOICE"))
if x==1:
    vit_stud={}
    y=int(input("ENTER NUMBER TO STUDENTS TO ENTER\n"))
    for i in range(y):
        em=input("ENTER EMAIL ID OF PERSON\n")
        vitvalid(em,vit_stud)
        print("\n")
    for i in vit_stud.keys():
        if vit_stud[i][1]=="YES":
            print("EMAIL_ID : ",vit_stud[i][0])
            print("REG. NO. : ",vit_stud[i][2])
            print("PHONE NO. : ",vit_stud[i][3])
            print("\n")
    print("THANK YOU :) ")
elif x==2:
    vit_stud={}
    ans2="y"
    while(ans2=="y"):
        em=input("ENTER EMAIL ID OF PERSON\n")
        vitvalid(em,vit_stud)
        print("\n")
        ans2=input("WANT TO ADD MORE?(y/n) : \n")
    for i in vit_stud.keys():
        if vit_stud[i][1]=="YES":
            print("EMAIL_ID : ",vit_stud[i][0])
            print("REG. NO. : ",vit_stud[i][2])
            print("PHONE NO. : ",vit_stud[i][3])
            print("\n")
    print("THANK YOU :)")

else:
    print("NOT A VALID INPUT,TRY AGAIN")
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




