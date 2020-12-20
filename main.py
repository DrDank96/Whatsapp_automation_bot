import pyautogui as pt
from time import sleep
import pyperclip
import random
wait_dur=0

#position1 = pt.locateOnScreen("C:\pemp_stuff\smile_paperclip.png" , confidence =.6)
#x = position1[0]
#y = position1[1]

# Gets message
# I copied this function from the tutorial that i was watching
def get_message():
   # global x, y
    position = pt.locateOnScreen("C:\pemp_stuff\smile_paperclip.png", confidence= .6)
    y = position[1]
    x = position[0]
    pt.moveTo(x,y)
    pt.tripleClick()
    pt.moveRel(32,-50,duration=wait_dur)
    pt.tripleClick(duration=wait_dur)
    pt.rightClick(duration=wait_dur)
    pt.moveRel(47,-127,duration=wait_dur)
    pt.click(duration=wait_dur)
    whats_mesg = pyperclip.paste()
    return whats_mesg

# Post Reply
#I copied this function from the tutorial that i was watching
def post_response(omessage,safe = 0):
    #global x, y
    position = pt.locateOnScreen("C:\pemp_stuff\smile_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200,y+20,duration=wait_dur)
    pt.click()
    pt.typewrite(omessage)
    if(safe==0):
        pt.typewrite("\n")



#All code from now on is mine own!!
#Formulates Replies
#Enter replies here
def proces_response(imessage,safe=0):
    if(safe==0):
        if(imessage=="Hello"):
            return "Hi"
        elif(imessage=="Hi"):
            return "Hello"
        else:
            return "none"
    else:
        if(imessage=="HHello"):
            return "Hi"
        elif(imessage=="WWatcha Doingg?"):
            return "Just chillin"
        elif(imessage=="HHi"):
            return "Hello"
        elif(imessage=="WWho Are Youu?"):
            return "Hi, i'm a bot desined by Mr. Harsh..!"
        else:
            return " "

def Check_new_chat(safe=0):
    #print(type(pt.locateOnScreen("C:\pemp_stuff\\big_green_circle.png", confidence= 0.8)))
   # print(None==(pt.locateOnScreen("C:\pemp_stuff\\big_green_circle.png", confidence= 0.8)))
    # return False
    if safe==0:
        if None == pt.locateOnScreen("C:\pemp_stuff\\big_green_circle.png", confidence=0.8):
            return False
        NCPosn = pt.locateOnScreen("C:\pemp_stuff\\big_green_circle.png", confidence=0.8)
        x = NCPosn[0]
        y = NCPosn[1]
        pt.moveTo(x, y, wait_dur)
        pt.click()
        return 1
"""
    elif safe==1:
        if None == pt.locateOnScreen("C:\pemp_stuff\mummy.png", confidence=0.8):
            return False
        NCPosn = pt.locateOnScreen("C:\pemp_stuff\mummy.png", confidence=0.8)
        x = NCPosn[0]
        y = NCPosn[1]
        pt.moveTo(x+20, y+10, wait_dur)
        pt.click()
        return 1
#"""

#this function is under construction, so i have'nt included it in the main program.
def Last_mesg():
    base_pos = pt.locateOnScreen("C:\pemp_stuff\smile_paperclip.png")
    pt.moveTo(base_pos[0],base_pos[1] - 150, wait_dur)
    while True:
        if pt.locateOnScreen("C:\pemp_stuff\\blue_tik.png", confidence= 0.6)==None:
            pt.vscroll(480)
        else:
            break
    position=pt.locateOnScreen("C:\pemp_stuff\\blue_tik.png", confidence= 0.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y,wait_dur)


#Last_mesg()
#just for fun , not requierd in actual program
#get_message()
def spam(text,n):
    i=0
    pt.moveTo(520,689)
    pt.click()
    while i<n:
        i+=1
        pt.typewrite(text)
        pt.typewrite("\n")

#print(get_message())
#"""

while True:
    sleep(0)
    x=Check_new_chat()
    if not x:
        print("skipped")
        continue
    iput= get_message()
    oput= proces_response(iput,1)
    post_response(oput)
    pt.moveTo(170,186,wait_dur)
    pt.click()


#"""