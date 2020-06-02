from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time
import os
#Settings
documentName = ""
columns = ""

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
    global documentName, documentUp, columns
    
    documentName = filedialog.askopenfilename( filetypes = (("Excel file", "*.xlsx"),("All files", "*.*")))
    documentData = pd.read_excel(documentName)
    columns = documentData.columns
    graphics(0,0, documentData)

    if documentName != "": 
        uploadedDocument.config(text = documentName.split('/')[-1]) 
        documentUp = True
    else: 
        uploadedDocument.config(text = "")
        documentUp = False
    
def graphics(x,y, DATA):
    x = []
    y = []
    fig = Figure(figsize=(7, 4), dpi= 100, facecolor= mainColor)
    choices = str(DATA.columns.ravel()).replace('[','').replace(']','').replace('\'','')
    
    xData = ttk.Combobox(root, values = choices)
    xData.place(x = barLimits[0]+120, y = 420)
    yData = ttk.Combobox(root, values = choices)
    yData.place(x = barLimits[0]+120, y = 460)
    xData.current(0)
    yData.current(0)
    for i in range(len(DATA[xData.get()])):
        x.append(DATA[xData.get()][i])
    for i in range(len(DATA[yData.get()])):
        y.append(DATA[yData.get()][i])
        
    fig.add_subplot(111).plot(x, y, color = "white", linewidth = 1)
    ax = fig.gca()
    
    ax.set_facecolor(mainColor)
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color(mainColor)
    ax.spines['right'].set_color(mainColor)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    xvariable.config(fg = "#E2A65C")
    yvariable.config(fg = "#E2A65C")
    if x == 0 and y == 0 :
        ax.spines['left'].set_color(mainColor)
        ax.spines['bottom'].set_color(mainColor)
        ax.tick_params(axis='x', colors=mainColor)
        ax.tick_params(axis='y', colors=mainColor)
        ax.yaxis.label.set_color(mainColor)
        ax.xaxis.label.set_color(mainColor)
        xvariable.config(fg = "#E2A65C")
        yvariable.config(fg = "#E2A65C")

    canvas = FigureCanvasTkAgg(fig, master=GraphicFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill= BOTH, expand=1)


root = Tk()

#Frames
mainArea = Frame(root, width = limits[0]-barLimits[0], height = limits[1], bg = mainColor)
mainArea.place(x = barLimits[0])
lateralBar = Frame(root, width = barLimits[0],height = barLimits[1], bg = barColor[0])
lateralBar.place(x = 0)
bottomBar = Frame(root, width = bottomLimits[0], height = bottomLimits[1], bg = bottomColor)
bottomBar.place(x = 0, y = limits[1]-bottomLimits[1])
GraphicFrame = Frame(mainArea, width = limits[0]-barLimits[0], height = limits[1]-200, bg = mainColor)
GraphicFrame.place(x = 0)
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
xvariable = Label(root, text = "X variable", font = "Verdana 12 bold", fg = mainColor, bg = mainColor, )
xvariable.place(x = barLimits[0]+10, y=420)
yvariable = Label(root, text = "Y variable", font = "Verdana 12 bold", fg = mainColor, bg = mainColor)
yvariable.place(x = barLimits[0]+10, y=460)


#drawGraphic = Button(root, text= "Draw", command = "graphics(x, y, DATA)")
#drawGraphic.place(x = barLimits[0]+280, y = 420)
#Code

#Geometry and loop
root.geometry(str(limits[0])+'x'+str(limits[1]))
root.resizable(width = False, height = False)
root.iconbitmap(currentDirectory+'/logo.ico')
root.title("PyStatistics v1.0")

root.mainloop()