import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd  # import pandas
import numpy as np

# Plotting the Input data
def funcGraph(arrValues, intReceiverNos, strTitle, strLabelX, strLabelY, intLimX, intLimY, strLegend, tabName):
    # the figure that will contain the plot
    figLinePlot = Figure(figsize = (9, 16), dpi = 120)
    # adding the subplot
    pltLinePlot = figLinePlot.add_subplot(111)
  
    # plotting the graph
    i = 0
    while i < intReceiverNos:
        pltLinePlot.plot(arrValues[:, i], label = strLegend + str(i + 1))
        i += 1

    pltLinePlot.set_xlim([0, intLimX])
    pltLinePlot.set_ylim([-0.5*intLimY, 0.5*intLimY])

    pltLinePlot.set_title(strTitle)
    pltLinePlot.set_xlabel(strLabelX)
    pltLinePlot.set_ylabel(strLabelY)
    pltLinePlot.legend()
  
    frmPlot = tk.Frame(tabName)
    frmToolbar = tk.Frame(tabName)
    frmPlot.place(relwidth = 1, relheight = 0.94, relx = 0.00, rely = 0.0)
    frmToolbar.place(relwidth = 1, relheight = 0.06, relx = 0.00, rely = 0.94)

    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(figLinePlot, master = frmPlot)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, frmToolbar)
    toolbar.update()

def funcHeatMap(ReflList, ArrSize, MaxDist, PhiSize, AngResol, tabName):
    arrDist = np.linspace(0, MaxDist, ArrSize)
    arrBearings = np.linspace(np.deg2rad(-70 + (AngResol/2)), np.deg2rad(70 - (AngResol/2)), PhiSize)
    rad, th = np.meshgrid(arrDist, arrBearings)
    
    # the figure that will contain the plot
    figHeatMap = Figure(figsize = (16, 9), dpi = 120)
    
    # adding the subplot
    pltHeatMap = figHeatMap.add_subplot(111, polar = True)
   
    pltHeatMap.set_theta_zero_location("N") # Set the zero location to north
    pltHeatMap.set_thetamin(-70)  # Set the minimum angle
    pltHeatMap.set_thetamax(70)   # Set the maximum angle
    pltHeatMap.set_xticks(np.deg2rad(np.arange(-70, 80, 10)))  # Set the x-axis tick locations
    # pltHeatMap.set_yticklabels([])  # To avoid coincidence of radial distance labels and -70 degrees label 
   
    pltHeatMap.set_title('Heat Map')
    pltHeatMap.set_xlabel('Angle', labelpad= -25)
    pltHeatMap.set_ylabel('Radial Distance', labelpad=30)  # Adjust the labelpad value to shift the label more to the left

    pltHeatMap.pcolormesh(th, rad, ReflList.T, cmap = "Reds", shading = "nearest")
    pltHeatMap.grid()
    
    # create a canvas for your plot and place it on your window
    frmHeatMap = tk.Frame(tabName)
    frmHeatMap.place(relwidth=0.94, relheight=0.94, relx=0.00, rely=0.0)

    # create a toolbar for your plot and place it on your window
    frmHeatMapToolbar = tk.Frame(tabName)
    frmHeatMapToolbar.place(relwidth=1, relheight=0.06, relx=0.00, rely=0.94)

    # creating the Tkinter canvas containing the Matplotlib figure
    canvasHeatMap = FigureCanvasTkAgg(figHeatMap, master=frmHeatMap)
    canvasHeatMap.draw()

    # placing the canvas on the Tkinter window
    canvasHeatMap.get_tk_widget().place(relwidth=1, relheight=1, relx=0.00, rely=0.00)

    # creating the Matplotlib toolbar
    toolbarHeatMap = NavigationToolbar2Tk(canvasHeatMap, frmHeatMapToolbar)
    toolbarHeatMap.update()

if __name__ == "__main__" :
    print("This is a module.\nThis should not be executed on standalone basis.")
