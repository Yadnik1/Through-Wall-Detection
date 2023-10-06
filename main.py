### Import tkinter module for GUI
import tkinter as tk
from tkinter import Frame
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox

### Import sys module for system functions
import sys

### Import csv module for processing csv data
import csv

### Import numpy for numerical computation
import numpy as np

### Import icons and logos from the module mdlImageStore.py
import mdlImageStore
from mdlImageStore import Icons

### Import graph from plots.py
# import mdlSettings

### Import GUI from the module mdlGUI.py
#import mdlGUI

### Import bearings claculation from plots.py
import mdlBearings

### Import graph from plots.py
import mdlPlots
from mdlPlots import funcGraph

#import ctypes
#ctypes.windll.shcore.SetProcessDpiAwareness(1)

### End - Imports

### Global variables for data procesing/generation/settings
global bolSkipSamples, bolRealtimeData

global intReceiversNos, intMaxDistance, intAngResolution
global intArraySize, intSamplesCorr
global intRealtimeData, intSNR

global arrPulseProfile, arrIntensityData, arrPhaseData, arrCorrMatrix

global fltWallThickness

global strWallMaterial, strWallProximity

### End - Global Declaration

### Initialise settings
if __name__ == "__main__":
    ### false uses stored data, true uses realtime data
    bolRealtimeData = False

    ### false uses all samples for correlation, true uses every 3rd sample
    bolSkipSamples = False

    ### Change Size of Certain Arrays according to the Skip Sample Condition
    intArraySize = 270
    # intArraySize = intArraySize//2 if bolSkipSamples else intArraySize

    ### Max Distance (metres) measured by the device
    intMaxDistance = 10

    ### Specifies the angular resolution (degrees)
    intAngResolution = 5

    ### Power Threshold Level In %
    intThresholdLevel = 80
    
    ### Shape of the pulse for 3-point correlation (sum of squares must be equal to 1)
    # arrPulseProfile = np.array([-0.4, 0.8, -0.447214])
    
    ### SNR level (dB)
    # intSNR = 5

    ### Number of consecutive samples used for correlation
    # intSamplesCorr = 1000
    
    ### Count Numbers of Iterations
    # intCounts = 0

### End - Initialisations

### Define the main window of the app
winMain = tk.Tk()
winMain.minsize(1280, 720)

### Calculate size and offset of the main window
intScreenWidth = winMain.winfo_screenwidth()
intScreenHeight = winMain.winfo_screenheight()
intWindowWidth = round((intScreenWidth/(1920/1280)))
intWindowHeight = round((intScreenHeight/(1080/720)))
intWindowWidthOffset = str(round((intScreenWidth/2)) - round((intScreenHeight/2)))
intWindowHeightOffset = str(round((intScreenHeight/2)) - round((intWindowHeight/2)) - round((intScreenHeight/20)))

window_size_position = str(intWindowWidth) + "x" + str(intWindowHeight) + "+" + str(intWindowWidthOffset) +  "+" + str(intWindowHeightOffset)
if intWindowWidth > 1280:
    window_size_position = str("1280" + "x" + "720")
#print (window_size_position)

### Create the images that would be used in the app
imgIcon = tk.PhotoImage(data = Icons.b64Icon)
imgLogo = tk.PhotoImage(data = Icons.b64Logo)
#imgTitle = tk.PhotoImage(data = Icons.b64Title)

### Create the main window for the app
winMain.tk.call("tk", "scaling", 1)
winMain.title("MicroSentry")
winMain.geometry(window_size_position)
winMain.iconphoto(True, PhotoImage(data=Icons.b64Icon))
winMain.option_add("*font", "Arial 12")

### Create the top frame container
#frmTop = tk.Frame(winMain, bg = "white", bd = 0, borderwidth = 3, width = round(intWindowWidth/28))
frmTop = tk.Frame(winMain, bg = "white", bd = 0, borderwidth = 3)
frmTop.place(relwidth = 1, relheight = 0.18, relx = 0.0, rely = 0.0)

### Create a label widget to display the logo of SAMEER at the top left
lblLogoLeft = tk.Label(frmTop,  bg = "white", image = imgLogo)
lblLogoLeft.place(relwidth = 0.12, relheight = 1, relx = 0.01, rely = 0.01)

### Create label widgets to display the name of SAMEER at the top
lblTitle1 = tk.Label(frmTop, text = "Society for Applied Microwave Electronics Engineering and Research", bg = "white", fg = "#0948A5", font=("Arial 32 bold"), anchor = "center", padx = 10, pady = 5) 
lblTitle2 = tk.Label(frmTop, text = "Ministry of Electronics & Information Technology", bg = "white", fg = "#000000", font=("Arial", 24), anchor = 'center', padx = 10, pady = 5) 
lblTitle3 = tk.Label(frmTop, text = "Government of India", bg = "white", fg = "#000000", font=("Arial", 24), anchor = 'center', padx = 10, pady = 5) 
lblTitle1.place(relwidth = 0.87, relheight = 0.6, relx = 0.12, rely = 0.0)
lblTitle2.place(relwidth = 0.87, relheight = 0.2, relx = 0.12, rely = 0.55)
lblTitle3.place(relwidth = 0.87, relheight = 0.2, relx = 0.12, rely = 0.8)

### Create the left container for the settings on the left
frmLeft = tk.Frame(winMain, bg = "white", bd = 5)
lbmLeft1 = tk.LabelFrame(frmLeft, text = "Operation Data", font = ("Arial 20 bold"), bg = "white", bd = 5)
lbmLeft2 = tk.LabelFrame(frmLeft, text = "Settings", font = ("Arial 20 bold"), bg = "white", bd = 5)
lbmLeft3 = tk.LabelFrame(frmLeft, text = "Stored Data", font = ("Arial 20 bold"), bg = "white", bd = 5)
frmLeft.place(relwidth = 0.20, relheight = 0.82, relx = 0.00, rely = 0.18)
lbmLeft1.place(relwidth = 0.99, relheight = 0.10, relx = 0.01, rely = 0.00)
lbmLeft2.place(relwidth = 0.99, relheight = 0.70, relx = 0.01, rely = 0.10)
lbmLeft3.place(relwidth = 0.99, relheight = 0.20, relx = 0.01, rely = 0.80)

intRealtimeData = tk.IntVar()

def selDataMode():

    bolRealtimeData = bool(intRealtimeData.get())
    #print(bool(intRealtimeData.get()))
    strMessage = "Realtime Data" if bolRealtimeData else "Stored Data"
    messagebox.showinfo(title = "Data Mode Selection", message = "Data mode changed has changed." + "\n" + "Selected option: " + strMessage)

### Create the radio buttons for the selection of data (Realtime/Stored)
intRealtimeData.set(False)
rbnRealtimeData = tk.Radiobutton(lbmLeft1, text = "Realtime", font = ("Arial 16"), bg = "#85C3DF", variable = intRealtimeData, value = True, command = selDataMode)
rbnStoredData = tk.Radiobutton(lbmLeft1, text = "Stored", font = ("Arial 16"), bg = "#85C3DF", variable = intRealtimeData, value = False, command = selDataMode)
rbnRealtimeData.place(relwidth = 0.48, relheight = 0.9, relx = 0.01, rely = 0.00)
rbnStoredData.place(relwidth = 0.48, relheight = 0.9, relx = 0.51, rely = 0.00)

def cbxWallThicknessChanged(event):
    fltWallThickness = float(0)
    #fltWallThickness = float(cbxWallThickness.get())
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {fltWallThickness}")

def cbxWallMaterialChanged(event):
    strWallMaterial = cbxWallThickness.get()
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {strWallMaterial}")

def cbxWallProximityChanged(event):
    strWallProximity = cbxWallProximity.get()
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {strWallProximity}")

def cbxReceiverNosChanged(event):
    intReceiverNos = int(cbxReceiverNos.get())
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {intReceiverNos}")

def cbxReceiversPitchChanged(event):
    fltReceiversPitch = float(cbxReceiversPitch.get())
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {fltReceiversPitch}")

def cbxWavelengthChanged(event):
    fltWavelength = float(0)
    #fltWavelength = float(cbxWavelength.get())
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {fltWavelength}")

def cbxSamplesPerIPPChanged(event):
    intSamplesPerIPP = int(cbxSamplesPerIPP.get())
    messagebox.showinfo(title = "New Selection", message=f"Selected option: {intSamplesPerIPP}")

### Change the default style of font and size of arrow for the combobox list
#fontComboBox = ("Arial 12")
##lbmLeft2.option_add('*TCombobox*Listbox.font', fontComboBox)   
#lbmLeft2.option_add("*TCombobox*.font", fontComboBox)   
styTTK = ttk.Style(lbmLeft2)
styTTK.theme_use("clam")
styTTK.configure("W.TCombobox", arrowsize = 20)

### Thickness of the wall
lblWallThickness = tk.Label(lbmLeft2, text = "Wall Thickness", bg = "#85C3DF", font = ("Arial 16")) 
cbxWallThickness = ttk.Combobox(lbmLeft2, values = ["5 cm", "10 cm", "15 cm", "20 cm", "25 cm"], style = "W.TCombobox")
cbxWallThickness.bind("<<ComboboxSelected>>", cbxWallThicknessChanged)
lblWallThickness.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.01)
cbxWallThickness.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.01)
cbxWallThickness.current(1)
fltWallThickness = float(1)

### Materials of construction of the wall
lblWallMaterial = tk.Label(lbmLeft2, text = "Wall Type", bg = "#85C3DF", font = ("Arial 16")) 
cbxWallMaterial = ttk.Combobox(lbmLeft2, values = ["Concrete", "Stone", "Brick", "Mud", "Wooden"], style = "W.TCombobox")
cbxWallMaterial.bind("<<ComboboxSelected>>", cbxWallMaterialChanged)
lblWallMaterial.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.13)
cbxWallMaterial.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.13)
cbxWallMaterial.current(0)
strWallMaterial = cbxWallMaterial.get()

### Proximity of the device to the wall
lblWallProximity = tk.Label(lbmLeft2, text = "Wall Proximity", bg = "#85C3DF", font = ("Arial 16")) 
cbxWallProximity = ttk.Combobox(lbmLeft2, values = ["1 cm", "2 cm", "4 cm", "8 cm", "16 cm", "32 cm", "64 cm"], style = "W.TCombobox")
cbxWallProximity.bind("<<ComboboxSelectedSelected>>", cbxWallProximityChanged)
lblWallProximity.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.25)
cbxWallProximity.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.25)
cbxWallProximity.current(0)
strWallProximity = cbxWallProximity.get()

### Number of receivers used in the device
lblReceiverNos = tk.Label(lbmLeft2, text = "Receivers", bg = "#85C3DF", font = ("Arial 16")) 
cbxReceiverNos = ttk.Combobox(lbmLeft2, values = ["2", "4", "6", "8"], style = "W.TCombobox")
cbxReceiverNos.bind("<<ComboboxSelectedSelected>>", cbxReceiverNosChanged)
lblReceiverNos.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.37)
cbxReceiverNos.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.37)
cbxReceiverNos.current(1)
intReceiverNos = int(cbxReceiverNos.get())

### Distance between the receivers in multiples of wavelength used
lblReceiversPitch = tk.Label(lbmLeft2, text = "Receiver's Pitch", bg = "#85C3DF", font = ("Arial 16")) 
cbxReceiversPitch = ttk.Combobox(lbmLeft2, values = ["0.44", "0.47", "0.50", "0.53", "0.56", "0.59"], style = "W.TCombobox")
cbxReceiversPitch.bind("<<ComboboxSelected>>", cbxReceiversPitchChanged)
lblReceiversPitch.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.49)
cbxReceiversPitch.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.49)
cbxReceiversPitch.current(3)
fltReceiversPitch = float(cbxReceiversPitch.get())

### Wavelength used in the device
lblWavelength = tk.Label(lbmLeft2, text = "Wavelength", bg = "#85C3DF", font = ("Arial 16")) 
cbxWavelength = ttk.Combobox(lbmLeft2, values = ["12.454", "12.403", "12.351", "12.300", "12.250", "12.200", "12.150", "12.101", "12.052", "12.004", "11.956"], style = "W.TCombobox")
cbxWavelength.bind("<<ComboboxSelected>>", cbxWavelengthChanged)
lblWavelength.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.61)
cbxWavelength.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.61)
cbxWavelength.current(5)
fltWavelength = float(cbxWavelength.get())

### No. of Samples/IPP
lblSamplesPerIPP = tk.Label(lbmLeft2, text = "Samples/IPP", bg = "#85C3DF", font = ("Arial 16")) 
cbxSamplesPerIPP = ttk.Combobox(lbmLeft2, values = ["100", "270", "350", "400"], style = "W.TCombobox")
cbxSamplesPerIPP.bind("<<ComboboxSelected>>", cbxSamplesPerIPPChanged)
lblSamplesPerIPP.place(relwidth = 0.48, relheight = 0.075, relx = 0.01, rely = 0.73)
cbxSamplesPerIPP.place(relwidth = 0.48, relheight = 0.075, relx = 0.51, rely = 0.73)
cbxSamplesPerIPP.current(1)
intSamplesPerIPP = int(cbxSamplesPerIPP.get())

def cmdOpenFileDialog():
    #### Open a dialog box, select a file
    global arrIntensityData, arrPhaseData
    global intDataSize

    filData = filedialog.askopenfilename(title = "Open a data file", initialdir = "G:\My Drive\Sales\Customers\SAMEER, Mumbai/", filetypes = (("data files", "*.csv"),("text files", "*.txt"),("All files", "*.*")))
    messagebox.showinfo("Selected data file ", filData)
    lblFileName.config(text = filData)

    with open(lblFileName.cget("text"), 'r') as filData:
        ### create a CSV reader object
        strDataFile = csv.reader(filData)
        
        strIntensityData = ""
        strPhaseData = ""
        intRowNumber = 0
        for row_number, row in enumerate(strDataFile):
            intRowNumber = row_number
            intDataSize = intRowNumber

        ### Create a array with no rows and no columns
        arrIntensityData = np.zeros((intRowNumber + 1, intReceiverNos))
        arrPhaseData = np.zeros((intRowNumber + 1, intReceiverNos))

        filData.seek(0)
        for row_number, row in enumerate(strDataFile):
            ### Add a new row to the array
            i = 0
            strTemp1 = ""
            strTemp2 = ""
            while i < intReceiverNos:
                arrIntensityData[row_number, i] = float(row[2*i])
                arrPhaseData[row_number, i] = float(row[2*i +  1])
                strTemp1 = strTemp1 + row[i] + ", " 
                strTemp2 = strTemp2 + row[2*i +1] + ", " 
                i += 1
            strIntensityData += strTemp1 + "\n"
            strPhaseData += strTemp2 + "\n"
            intRowNumber = row_number
            #print(f"Row {row_number}: {row}")
        
        #lblIntensityData.config(text = strIntensityData)
        #lblPhaseData.config(text = strPhaseData)

        ### close the file
        filData.close()
        print("No. of row read = ", str(intRowNumber))

def cmdProcessData():
    # Process the selected file
    global arrAvgMatrix

    messagebox.showinfo("Processing data file \n", lblFileName.cget("text"))
    
    ### Change Size of Certain Arrays according to the Skip Sample Condition
    intArraySize = intSamplesPerIPP//2 if bolSkipSamples else intSamplesPerIPP
    intReceiverNos = int(cbxReceiverNos.get())

    arrAvgMatrix = np.zeros((intArraySize, intReceiverNos)).astype("complex")
    
    i = 0
    j = 0
    strTemp1 = ""
    strTemp2 = ""
    while i < intDataSize:
        while j < intArraySize:
            arrAvgMatrix[j, :].real += arrIntensityData[i, :]
            arrAvgMatrix[j, :].imag += arrPhaseData[i, :]
            i += 1
            j += 1
        #print(arrAvgMatrix[j-1, :])
        j = 0
    
    arrAvgMatrix[:,:] = arrAvgMatrix[:,:]/((intDataSize+1)/intArraySize)
    # print(arrAvgMatrix)
    #print(intDataSize+1, intArraySize, (intDataSize+1)/intArraySize)

    funcGraph(arrIntensityData, intReceiverNos, "Received Data", "Number of Samples (No)", "Voltage (V)", 5400, 1, "I", tabIntensityData)
    funcGraph(arrPhaseData, intReceiverNos, "Received Data", "Number of Samples (No)", "Voltage (V)", 5400, 1, "Q", tabPhaseData)

    funcGraph(arrAvgMatrix.real, intReceiverNos, "Received Data", "Number of Samples (No)", "Voltage (V)", intArraySize, 1, "I", tabCorrelatedIntensity)
    funcGraph(arrAvgMatrix.imag, intReceiverNos, "Received Data", "Number of Samples (No)", "Voltage (V)", intArraySize, 1, "Q", tabCorrelatedPhase)
    
    ### Initialize Bearing Calculations Outside Loop
    clsBearings = mdlBearings.clsBearings(intArraySize, fltReceiversPitch, intReceiverNos, intAngResolution, intThresholdLevel)
    clsBearings.funcGenPhi()
    clsBearings.funcGenPathMatrix()

    ### Invert Path Matrix
    clsBearings.funcInvertMatrix()
    
    for i in range(intArraySize):
        clsBearings.funcGetRefl(i, arrAvgMatrix[i].transpose())
        
    # plots.plot_heat(bearing_matrix.refl_list, corr_arr_size, max_dist, len(bearing_matrix.phi), counts, plt.figure(3), ang_resol)
    mdlPlots.funcHeatMap(clsBearings.ReflList, intArraySize, intMaxDistance, len(clsBearings.Phi), intAngResolution, tabHeatMap)


# Create a button to open the dialog box
lblFileName = tk.Label(lbmLeft3, text = "filename", bg = "white", font = ("Arial 12"), borderwidth = 2, relief = "sunken", wraplength = 240) 
btnSelectData = tk.Button(lbmLeft3, text = "Select Data", font = ("Arial 16"), bg = "#85C3DF", command = cmdOpenFileDialog)
btnProcessData = tk.Button(lbmLeft3, text = "Process Data", font = ("Arial 16"), bg = "#85C3DF", command = cmdProcessData)
lblFileName.place(relwidth = 0.94, relheight = 0.55, relx = 0.02, rely = 0.01)
btnSelectData.place(relwidth = 0.45, relheight = 0.3, relx = 0.02, rely = 0.65)
btnProcessData.place(relwidth = 0.45, relheight = 0.3, relx = 0.52, rely = 0.65)

# Create the main container (graphs)
frmMain = tk.Frame(winMain, bg = "#85C3DF", bd = 2)
tabMain = ttk.Notebook(frmMain)
tabIntensityData = ttk.Frame(tabMain)
tabPhaseData = ttk.Frame(tabMain)
tabIntensityCorr = ttk.Frame(tabMain)
tabCorrelatedIntensity = ttk.Frame(tabMain)
tabCorrelatedPhase = ttk.Frame(tabMain)
tabReflectivity = ttk.Frame(tabMain)
tabHeatMap = ttk.Frame(tabMain)

style = ttk.Style()
style.configure('TNotebook.Tab', font = ("Arial 16 bold"))

lblAppName = tk.Label(frmMain, text = "Microwave Based Through-The-wall Detection", bg = "white", font = ("Arial 16 bold"), borderwidth = 1, relief = "sunken", anchor = "center") 
frmMain.place(relwidth = 0.80, relheight = 0.76, relx = 0.20, rely = 0.18)
lblAppName.place(relwidth = 1, relheight = 0.05, relx = 0.0, rely = 0.0)
tabMain.place(relwidth = 1, relheight = 0.95, relx = 0.0, rely = 0.05)

tabMain.add(tabIntensityData, text = "Intensity Data (I)")
#lblIntensityData = tk.Label(tabIntensityData, text = "Data not read", bg = "white", font = ("Terminal 12"), borderwidth = 1, relief = "sunken", anchor = "nw") 
#lblIntensityData.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

tabMain.add(tabPhaseData, text = "Phase Data (Q)")
#lblPhaseData = tk.Label(tabPhaseData, text = "Data not read", bg = "white", font = ("Terminal 12"), borderwidth = 1, relief = "sunken", anchor = "nw") 
#lblPhaseData.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

tabMain.add(tabCorrelatedIntensity, text = "Correlated Data (I)")
#imgCorrelatedData = tk.PhotoImage(file = "C:\Workspace\TrialsUI\Images\InputData-28Apr2022a.png")
#lblCorrelatedData = tk.Label(tabCorrelatedData, image = imgCorrelatedData)
#lblCorrelatedData.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

tabMain.add(tabCorrelatedPhase, text = "Correlated Data (Q)")
#imgCorrelatedData = tk.PhotoImage(file = "C:\Workspace\TrialsUI\Images\InputData-28Apr2022a.png")
#lblCorrelatedData = tk.Label(tabCorrelatedData, image = imgCorrelatedData)
#lblCorrelatedData.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

tabMain.add(tabReflectivity, text = "Reflectivity Plot")
imgReflectivity = tk.PhotoImage(file = "Reflectivity-28Apr2022a.png")
lblReflectivity = tk.Label(tabReflectivity, image = imgReflectivity)
lblReflectivity.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

tabMain.add(tabHeatMap, text = "Heat Map")
imgHeatMap = tk.PhotoImage(file = "HeatMap-28Apr2022a.png")
lblHeatMap = tk.Label(tabHeatMap, image = imgHeatMap)
lblHeatMap.place(relwidth = 1, relheight = 1, relx = 0.00, rely = 0.00)

# Create the bottom container (exit)
def cmdQuitApp():
   # Quit the App
    res = messagebox.askquestion("Closing the app", "Are you sure ?")
    if res == 'yes':
        sys.exit("User Exit")   
   
frmBottom = tk.Frame(winMain, bg = "white")
btnQuitApp = tk.Button(frmBottom, text = "Quit App", font=("Arial", 16), bg = "#85C3DF", fg = "red",  command = cmdQuitApp)
btnQuitApp.place(relwidth = 0.08, relheight = 0.6, relx = 0.7, rely = 0.2)

lblDeveloper = tk.Label(frmBottom, text = "Devlata Technologies Pvt Ltd", bg = "white", fg = "#0948A5", font = ("Arial 12")) 
lblEmail = tk.Label(frmBottom, text = "info@devlata.com", bg = "white", fg = "#0948A5", font = ("Arial 12")) 
frmBottom.place(relwidth = 0.80, relheight = 0.06, relx = 0.20, rely = 0.94)
lblDeveloper.place(relheight = 0.20, relx = 0.99, rely = 0.3, anchor = "e")
lblEmail.place(relheight = 0.20, relx = 0.99, rely = 0.7, anchor = "e")

winMain.mainloop()
