import numpy as np 
from Ruido import Desplazamiento, noise
from pathlib import Path

# Definimos la función gaussiana para simular los picos de los espectros 
def gaussian(x, mu, sigma=80):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))

# Cargamos los datos reales y definimos los canales
data = np.loadtxt("Datos reales\MCA_data.dat")  #Datos reales  
Canales = np.linspace(0, data[:, 0].size, data[:, 0].size+1)  

# Definimos los picos de los espectros para cada isótopo
mu_Pu = 3380  # 239Pu
mu_Am = 3600  # 241Am
mu_Cm = 3800  # 244Cm

Pu_dist = gaussian(Canales , mu_Pu) # 239Pu
Am_dist = gaussian(Canales, mu_Am) # 241Am
Cm_dist = gaussian(Canales, mu_Cm) # 244Cm

Total_dist = Pu_dist*0.83 + Am_dist*0.76 + Cm_dist*0.68

#Generamos un arreglo de temperaturas aleatorias y simulamos los datos ruidosos y desplazamiento debido a cada temperatura
Temperaturas = np.random.randint(0, 10, size=100) 

#inicializamos los arreglos para almacenar los datos simulados y los datos ruidosos
Datos = np.zeros((Temperaturas.size, Canales.size))   
Datos_ruidosos = np.zeros((Temperaturas.size, Canales.size))

# Creamos un directorio para almacenar los datos simulados
out_dir = Path("Datos sinteticos")
out_dir.mkdir(exist_ok=True) # Directorio de salida para los datos simulados

# Simulamos los datos para cada temperatura y los guardamos en archivos separados
for i in range(Temperaturas.size):
    DT = Desplazamiento(Temperaturas[i]) #Funcion que genera un desplazamiento aleatorio en el espectro debido a la temperatura
    Datos[i] = gaussian(Canales , mu_Pu + DT) * 0.83 + gaussian(Canales , mu_Am + DT) * 0.76 + gaussian(Canales , mu_Cm + DT) * 0.68
    # Agregamos ruido a los datos simulados
    Datos_ruidosos[i] = noise(Datos[i], 400)
    # Guardamos los datos simulados y ruidosos en archivos separados
    write_data = np.column_stack((Canales, Datos_ruidosos[i]))
    np.savetxt(out_dir / f"Datos_simulados_{i}.dat", write_data, fmt='%.2f')