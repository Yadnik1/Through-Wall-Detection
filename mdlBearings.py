import numpy as np
from cmath import rect
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class clsBearings:

    def __init__(self, ArrSize, RxDist, RxNo, AngResol, ThresLevel):
       self.ArrSize = ArrSize
       self.RxDist = RxDist
       self.RxNo = RxNo
       self.AngResol = AngResol
       self.ThresLevel = ThresLevel
       self.ReflList = np.zeros((self.ArrSize, int(140/self.AngResol)))

       print(self.ArrSize, self.RxDist, self.RxNo, self.AngResol, self.ThresLevel) 

    ### Generates the required phi values for bearing calculation
    def funcGenPhi(self):
        self.Phi = []
        ### Generate phi values for path matrix
        for theta in range(-70, 70, self.AngResol):
            valPhi = self.RxDist * np.sin(np.deg2rad(theta + (self.AngResol/2))) * 2 * np.pi
            self.Phi.append(valPhi)

    ### Generates the path matrix
    def funcGenPathMatrix(self):
        self.PathMatrix = np.zeros((self.RxNo, len(self.Phi))).astype('complex')
        for i in range(self.RxNo):
            for j in range(len(self.Phi)):
                self.PathMatrix[i][j] = rect(1, self.Phi[j] * i)

    ### Matrix Inversion using Psuedo-Inverse (SVD)
    def funcInvertMatrix(self):
        self.InvertedPath = np.linalg.pinv(self.PathMatrix)
        # return self.inv_p
        
    ### Calculation of the Reflectivity Vector
    def funcGetRefl(self, i, x):
        # print(type(self.inv_p))
        
        self.ReflMatrix = np.matmul(self.InvertedPath, x)

        ### Power Level Thresholding
        peak = np.amax(abs(self.ReflMatrix))
        mask = (abs(self.ReflMatrix) < (peak/np.sqrt(100/self.ThresLevel))) | (abs(self.ReflMatrix) > peak)
        self.threshed_mat = abs(self.ReflMatrix).copy()
        self.threshed_mat[mask] = 0
        self.ReflList[i] = self.threshed_mat

        # print(abs(self.ReflMatrix))
        # print(np.argmax(self.refl_mat))
        # Create a new figure
        # Create a new figure
        # fig = plt.figure()
        # plt.xlabel("Bearing Angle")
        # plt.plot(np.arange(-65, 71, 5), abs(self.ReflMatrix), label=i)
        # plt.title("Reflectivity Vector")
        # plt.savefig('pics/Reflectivity_Vector.png', bbox_inches='tight')
        # plt.show()
    ### End of Function
### End of Class

if __name__ == "__main__" :
    print("This is a module.\nThis should not be executed on standalone basis.")

