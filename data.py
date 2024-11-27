import pandas as pd

# Cargar archivo
path = "E:\\TripleTen\\Data Scients\\Sprint_7\\Proyecto\\"
archivo = path + 'vehicles_us.csv'

data_base = pd.read_csv(archivo)
print(data_base.head())