import numpy as np
import joblib
import pandas as pd

from pathlib import Path

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error

def preprocesar(cuentas):
    v = cuentas[lo:hi].reshape(-1, bin_size).sum(axis=1).astype(float)
    v = np.sqrt(v)                 
    return v / v.sum()   

out_dir = Path("Datos sinteticos")
etiq = np.loadtxt(out_dir / "etiquetas.csv", delimiter=",", skiprows=1)
DT = etiq[:, 2]

lo, hi, bin_size = 2500, 4500, 4   

         

X = np.array([preprocesar(np.loadtxt(out_dir / f"Datos_simulados_{int(i)}.dat")[:, 1]) for i in etiq[:, 0]])
y = DT / 200                      

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

PrimeraCapa = 4
SegundaCapa = 2

modelo = make_pipeline(StandardScaler(), MLPRegressor(hidden_layer_sizes=(PrimeraCapa, SegundaCapa), early_stopping=True, max_iter=500, random_state=42), )
modelo.fit(Xtr, ytr)

joblib.dump(modelo, Path("Modelos") / f"modelo_DT_{PrimeraCapa},{SegundaCapa}.joblib")

pred = modelo.predict(Xte) * 200
MAE = mean_absolute_error(yte * 200, pred)
print("MAE en DT (canales):", MAE)

MAEModelo = pd.DataFrame({"Modelo(Capas)": [(PrimeraCapa, SegundaCapa)], "MAE": [MAE]})

MAEModelo.to_csv(Path("Modelos") / "ModelosMae.csv", mode = "a", index=False, header=False)