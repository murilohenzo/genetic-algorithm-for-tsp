import numpy as np
import pandas as pd

populacao = []
for i in range(100):
    individuo = np.arange(1, 100)
    np.random.shuffle(individuo)
    individuo = np.insert(individuo, 0, 0)
    individuo = np.insert(individuo, 100, 0)
    populacao.append(individuo)

coordenadas = {'latitude': populacao[0],
               'longitude': populacao[1]}

df = pd.DataFrame(coordenadas, columns=['latitude', 'longitude'])
df.to_csv("coordenadas.csv")

