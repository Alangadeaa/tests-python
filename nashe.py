import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tupla = {'15', '16', '17', '21'}
lista = [1, 2, 3, 4, 5]
aula = {'nombre':['jose', 'josei', 'joseee', 'joseuue'], 'edad':['15', '16', '17', '21'], 'califi':['10', '9', '6', '7']}
print(aula)
pd.DataFrame(aula)
data = pd.DataFrame(aula)
data[['nombre']] 
data[['edad']] 
mascara_ageless18 = data['edad'] < '18'
data[mascara_ageless18]
mascara_agelesss18 = (data[['edad']] < '18') & (data[['edad']] > '15')
data[mascara_agelesss18]
datata = data[['edad']] 
datata.min()
datata.max()
plt.plot([1, 2, 3, 4, 5],[6, 7, 2, 9, 3])
plt.plot([1, 2, 3, 4, 5],[6, 7, 2, 9, 3], linestyle='-.')