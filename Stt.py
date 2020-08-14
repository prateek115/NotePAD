from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
from datetime import datetime
import speech_recognition as sr
import os

def newfile():
    global file
    window.title("Untitle-Notepad")
    file = None
    Textarea.delete(1.0,END)

def openfile():
    global file
    file= askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documnet","*.txt")])
    if file=="":
        file=None
    else:
        window.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,'r')
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitle.txt",defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documnet","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            window.title(os.path.basename(file)+"-Notepad")
            print("File saved")
    else:
        f=open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()

def Exit_Notepad():
    window.destroy()

def Cut_func():
    Textarea.event_generate(("<<Cut>>"))

def Copy_func():
    Textarea.event_generate(("<<Copy>>"))

def Paste_func():
    Textarea.event_generate(("<<Paste>>"))

def Time():
    now=datetime.now()
    Textarea.insert(1.0,now)

def About():
    showinfo("Notepad","Made using python for practise purpose")

def STT():
    text=sr.Recognizer()
    with sr.Microphone() as source:
        print("say...")
        text.pause_threshold=1.0
        audio=text.listen(source)
        try:
            phrase=text.recognize_google(audio,language="en-in")
            Textarea.insert(INSERT,phrase + " ")
        except:
            showinfo("Nontepad","Sorry, not able to recognize. Say it again")

window=Tk()
window.title("Untitle-Notepad")
window.geometry("644x600")
window.wm_iconbitmap("not2.ico")
Textarea=Text(window , font="lucida")
Textarea.pack(expand=True, fill=BOTH)
file= None

menubar = Menu(window)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Exit",command=Exit_Notepad)

menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar , tearoff=0)
editmenu.add_command(label="Cut",command=Cut_func)
editmenu.add_command(label="Copy",command=Copy_func)
editmenu.add_command(label="Paste",command=Paste_func)
editmenu.add_command(label="Date/Time",command=Time)

menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=About)

menubar.add_cascade(label="Help",menu=helpmenu)

speechmenu=Menu(menubar,tearoff=0)
speechmenu.add_command(label="Speech to text",command=STT)
menubar.add_cascade(label="Speech",menu=speechmenu)

window.config(menu=menubar)

scroll=Scrollbar(Textarea)
scroll.pack(side=RIGHT , fill=Y)
scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scroll.set)

window.mainloop()
