import numpy as np

data = np.loadtxt("Datos reales\MCA_Data_01.dat")  #Datos reales  

for i in range(1, data.shape[1]):
    if np.array_equal(data[:, i], data[:, i-1]):
        print(f"Los datos de las columnas {i} y {i-1} son iguales")