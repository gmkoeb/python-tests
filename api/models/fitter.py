import numpy as np 
import os
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq 
from sklearn.metrics import r2_score 

class Fitter:
    def __init__(self):
        pass
    
    def _theoretical_function(self, a, b, c, x, y):
        return (a*(np.exp(b*(x-y*c))-1)) 
    
    def _residuum(self, params, x, y): 
        a, b, c = params[0], params[1], params[2]
        residual = y-self._theoretical_function(a, b, c, x, y)
        return residual
    
    def _fit(self, x, y, params):
        result = leastsq(self._residuum, params, (x, y)) 
        a, b, c = result[0][0], result[0][1], result[0][2]
        yfit = self._theoretical_function(a, b, c, x, y)
        correlation_matrix = np.corrcoef(y, yfit)
        correlation_xy = correlation_matrix[0,1]
        r2 = correlation_xy**2
        return yfit, r2
    
    def plot(self, data_file):
        data = np.loadtxt(data_file) 
        x = data[:, 0]
        y = data[:, 1]

        params = [0.000005, 0.1, 100] 
 
        yfit, r2 = self._fit(x, y, params)

        plt.plot(x, yfit, 'r-', label="Fit")
        plt.plot(x, y, 'bo', markevery=20, label="Experimental")
        plt.title('Fit')
        plt.xlabel('V(V)')
        plt.ylabel('J(A/m²)')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(loc='best', fancybox=True, shadow=True)
        plt.tight_layout()
        filename = os.path.basename(data_file)
        plot_path = os.path.join('plots', f'{filename}.png')
        plt.savefig(plot_path)
        return r2
