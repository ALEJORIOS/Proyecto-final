import pandas as pd
from tkinter import *
from tkinter import filedialog
import time
import os
documentName = ""
#Variables
currentDirectory = os.getcwd().replace('\\','/')+'/Proyecto final'
documentUp = False
limits = [1000, 600]
barLimits = [298, limits[1]]
bottomLimits = [limits[0], 20]
mainColor = "#1E1E1E"
barColor = ["#252526", "#37373D"]
bottomColor = "#007ACC"
def getCurrentTime():
    currentTime = time.strftime('%H:%M:%S')
    getTime.config(text = currentTime)
    getTime.after(250, getCurrentTime)
def uploadData(): #Select the file and get the root
    global documentName, documentUp
    documentName = filedialog.askopenfilename( filetypes = (("Excel file", "*.xlsx"),("All files", "*.*")))
    if documentName != "": 
        uploadedDocument.config(text = documentName.split('/')[-1]) 
        documentUp = True
    else: 
        uploadedDocument.config(text = "")
        documentUp = False
    
root = Tk()

#Frames
mainArea = Frame(root, width = limits[0]-barLimits[0], height = limits[1], bg = mainColor)
mainArea.place(x = barLimits[0])
lateralBar = Frame(root, width = barLimits[0],height = barLimits[1], bg = barColor[0])
lateralBar.place(x = 0)
bottomBar = Frame(root, width = bottomLimits[0], height = bottomLimits[1], bg = bottomColor)
bottomBar.place(x = 0, y = limits[1]-bottomLimits[1])
#Buttons and Labels
getTime = Label(root, text = '00:00:00', bg = bottomColor, fg = "white")
getTime.place(x = limits[0]-50, y = limits[1]-20)
getCurrentTime()
uploadButton = Button(root, text = 'Upload data from PC', command=uploadData, bd = "0px", width = 24, bg = barColor[0], fg="White", font="Calibri 16 bold", activebackground = barColor[1], activeforeground = "white",anchor = 'w', padx = 15, justify = "left", cursor = "hand2")
uploadButton.place(x=0,y=100)
getRealTimeDataButton = Button(root, text = 'Get real-time data', command=uploadData, bd = "0px", width = 24, bg = barColor[0], fg="White", font="Calibri 16 bold", activebackground = barColor[1], activeforeground = "white",anchor = 'w', padx = 15, justify = "left", cursor = "hand2")
getRealTimeDataButton.place(x=0,y=150)
documentNameLabel = Label(root, text = 'PyStatistics Interface v 1.0', font = "Helvetica 16", fg = "#E2A65C", bg = barColor[0])
documentNameLabel.place(x = 15,y = 30)
uploadedDocument = Label(root, text = "", font = "Verdana 9", fg = "white", bg = bottomColor)
uploadedDocument.place(x = 10, y = limits[1]-20)
#Code

#Geometry and loop
root.geometry(str(limits[0])+'x'+str(limits[1]))
root.resizable(width = False, height = False)
root.iconbitmap(currentDirectory+'/logo.ico')
root.title("PyStatistics v1.0")

root.mainloop()