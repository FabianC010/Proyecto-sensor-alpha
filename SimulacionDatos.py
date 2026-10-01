import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt("Datos reales\MCA_data.dat")  #Datos reales  

def gaussian(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))

Canales = np.linspace(0, data[:, 0].size, data[:, 0].size+1)    


sigma = 80

Pu_dist = gaussian(Canales , mu=5155, sigma=sigma) # 239Pu
Am_dist = gaussian(Canales, mu=5486, sigma=sigma) # 241Am
Cm_dist = gaussian(Canales, mu=5805, sigma=sigma) # 244Cm

Total_dist = Pu_dist*0.73 + Am_dist*0.86 + Cm_dist*0.73

plt.figure(figsize=(12, 6)) 
plt.plot(Canales, Total_dist, label='Total', color='black')
plt.xlabel("Canales")
plt.title("Distribucion gaussianna simulada preliminar")
plt.legend()
plt.grid(True)
plt.show()
