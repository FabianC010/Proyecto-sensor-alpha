import numpy as np

def noise(Total_dist, intensidad):
    expected_counts = Total_dist / Total_dist.max() * intensidad
    return np.random.poisson(expected_counts)

def Desplazamiento(DT):
    return np.random.rand() * DT
    