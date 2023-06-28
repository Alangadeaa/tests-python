import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sitios-de-wifi.csv')
data = pd.DataFrame(df)

df.replace(to_replace="Dsiponible",
           value="Disponible", inplace = True)

df.replace(to_replace="Hospitales",
           value="Hospital", inplace = True)
df.drop({"etapa", "calle_cruce", 'codigo_postal', 'codigo_postal_argentino', 'objeto'}, axis=1, inplace=True)

pd.DataFrame(df)
estadodisp = (data['estado'] == 'Disponible')
comunas = (data['comuna'])
m = estadodisp & comunas
sns.countplot(data=data[m], y='comuna')
data['calle_nombre']
callesnashe = data['calle_nombre'].value_counts() > 8
callesnashe
callemayor8 = data['calle_nombre'].value_counts()[callesnashe]
sns.barplot(x= callemayor8, y= callemayor8.index)
plt.plot(data['calle_nombre'].value_counts())
call = (data['calle_nombre'].value_counts())