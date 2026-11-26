import numpy as np 
from pathlib import Path

np.random.seed(42)   # Fijamos la semilla para reproducibilidad

# Definimos la función gaussiana para simular los picos de los espectros 
def gaussian(x, mu, sigma=80):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))

def noise(Total_dist, intensidad):
    expected_counts = Total_dist / Total_dist.max() * intensidad
    return np.random.poisson(expected_counts)

def Desplazamiento(DT):
    return np.random.rand() * DT

# Cargamos los datos reales y definimos los canales
data = np.loadtxt(r"Datos reales\MCA_Data_01.dat")  #Datos reales  
Canales = np.arange(data.shape[0])
# Definimos los picos de los espectros para cada isótopo
mu_Pu, mu_Am, mu_Cm = 3380, 3600, 3800
#Generamos un arreglo de temperaturas aleatorias y simulamos los datos ruidosos y desplazamiento debido a cada temperatura
Temperaturas = np.random.randint(-200, 201, size=15000) 

# Creamos un directorio para almacenar los datos simulados
out_dir = Path("Datos sinteticos")
out_dir.mkdir(exist_ok=True) # Directorio de salida para los datos simulados
etiquetas = []

for i, T in enumerate(Temperaturas):
    DT = Desplazamiento(T)
    espectro = (0.83 * gaussian(Canales, mu_Pu + DT)
              + 0.76 * gaussian(Canales, mu_Am + DT)
              + 0.68 * gaussian(Canales, mu_Cm + DT))
    cuentas = noise(espectro, 400)
    np.savetxt(out_dir / f"Datos_simulados_{i}.dat", np.column_stack((Canales, cuentas)), fmt="%d")
    etiquetas.append((i, T, DT))

np.savetxt(out_dir / "etiquetas.csv", etiquetas, delimiter=",", header="indice,T,DT", comments="", fmt=["%d", "%d", "%.3f"])

