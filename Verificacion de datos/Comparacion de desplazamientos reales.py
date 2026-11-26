import numpy as np
from pathlib import Path
from scipy import signal as sg
from scipy.ndimage import gaussian_filter as gf

data = np.loadtxt(Path("./Datos reales") / "MCA_Data_01.dat")  #Datos reales  

min , max = 3000,4000
nPicos = 3

posiciones = np.full((nPicos, data.shape[1]), np.nan)

for i in range(data.shape[1]):
     DataS = gf(data[:,i], sigma = 2)
     idx, props = sg.find_peaks(data[min:max,i], height=10, distance=100, prominence=30)

     top = np.argsort(props["prominences"])[-nPicos:]
     posiciones[:, i] = np.sort(idx[top]) + min 

DesplazamientoPu = np.diff(posiciones[0])
DesplazamientoAm = np.diff(posiciones[1])
DesplazamientoCm = np.diff(posiciones[2])

DesplazamientoPromPu, DesplazamientoPromAm, DesplazamientoPromCm= np.nanmean(DesplazamientoPu), np.nanmean(DesplazamientoAm), np.nanmean(DesplazamientoCm)

print(f"El deplazamiento promedio del pico del Pu es :" ,DesplazamientoPromPu)
print(f"El deplazamiento promedio del pico del Am es :" ,DesplazamientoPromAm)
print(f"El deplazamiento promedio del pico del Cm es :" ,DesplazamientoPromCm)
