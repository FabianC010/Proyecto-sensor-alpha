import numpy as np 
from scipy import signal as sg
from pathlib import Path
# Cargamos los datos reales y definimos los canales
data = np.loadtxt(r"Datos reales\MCA_Data_01.dat")  #Datos reales  
Canales = np.arange(data.shape[0])
# Definimos los picos de los espectros para cada isótopo
mu_Pu, mu_Am, mu_Cm = 3380, 3600, 3800

