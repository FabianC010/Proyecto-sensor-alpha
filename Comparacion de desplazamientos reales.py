import numpy as np

data = np.loadtxt("Datos reales\MCA_data.dat")  #Datos reales  
Canales = np.linspace(0, data[:, 0].size, data[:, 0].size+1)  

PrimerPico = np.zeros(data.shape[1])
SegundoPico = np.zeros(data.shape[1])
TercerPico = np.zeros(data.shape[1])
for i in range(data.shape[1]):
    PrimerPico[i] = np.argmax(data[3300:3450,i]) 
    SegundoPico[i] = np.argmax(data[3500:3700,i])
    TercerPico[i] = np.argmax(data[3700:3900,i])

Desplazamiento_Pu = np.zeros(data.shape[1])
Desplazamiento_Am = np.zeros(data.shape[1])
Desplazamiento_Cm = np.zeros(data.shape[1])
print("Si el desplazamiento es positivo, el pico se desplaza a la derecha\n Si el desplazamiento es negativo, el pico se desplaza a la izquierda")
for i in range(1, data.shape[1]):
    Desplazamiento_Pu[i] = PrimerPico[i] - PrimerPico[i-1]
    Desplazamiento_Am[i] = SegundoPico[i] - SegundoPico[i-1]
    Desplazamiento_Cm[i] = TercerPico[i] - TercerPico[i-1]
    print("------------------------------")
    print(f"Desplazamiento del pico de Pu toma {i} con respecto a la toma {i-1}: {Desplazamiento_Pu[i]}")
    print(f"Desplazamiento del pico de Am toma {i} con respecto a la toma {i-1}: {Desplazamiento_Am[i]}")
    print(f"Desplazamiento del pico de Cm toma {i} con respecto a la toma {i-1}: {Desplazamiento_Cm[i]}")
    print("------------------------------")

