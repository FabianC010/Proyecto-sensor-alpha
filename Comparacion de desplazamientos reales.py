import numpy as np

data = np.loadtxt("Datos reales\MCA_Data_01.dat")  #Datos reales  

PrimerPico = np.zeros(data.shape[1])
SegundoPico = np.zeros(data.shape[1])
TercerPico = np.zeros(data.shape[1])
for i in range(data.shape[1]):
    if i<25:
        PrimerPico[i] = np.argmax(data[3200:3420,i]) 
        SegundoPico[i] = np.argmax(data[3400:3600,i])
        TercerPico[i] = np.argmax(data[3650:3900,i])
    else:
        PrimerPico[i] = np.argmax(data[3200:3420,i]) 
        SegundoPico[i] = np.argmax(data[3400:3600,i])
        TercerPico[i] = np.argmax(data[3600:3800,i])

DesplazamientoPu = np.zeros(data.shape[1])
DesplazamientoAm = np.zeros(data.shape[1])
DesplazamientoCm = np.zeros(data.shape[1])
print("Si el desplazamiento es positivo, el pico se desplaza a la derecha\n Si el desplazamiento es negativo, el pico se desplaza a la izquierda")
for i in range(1, data.shape[1]):
    DesplazamientoPu[i] = PrimerPico[i] - PrimerPico[i-1]
    DesplazamientoAm[i] = SegundoPico[i] - SegundoPico[i-1]
    DesplazamientoCm[i] = TercerPico[i] - TercerPico[i-1]
DesplazamientoPromPu = np.mean(DesplazamientoPu)
DesplazamientoPromAm = np.mean(DesplazamientoAm)
DesplazamientoPromCm = np.mean(DesplazamientoCm)
print(f"El deplazamiento promedio del pico del Pu es :" ,DesplazamientoPromPu)
print(f"El deplazamiento promedio del pico del Am es :" ,DesplazamientoPromAm)
print(f"El deplazamiento promedio del pico del Cm es :" ,DesplazamientoPromCm)
