import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data = np.random.rand(4,6)
print(data)
heatmap = sb.heatmap(data)
plt.show()
df = pd.read_csv(r"C:\Users\HampoJohnPaulAC\Downloads\Hash Analytic\gapminder-FiveYearData.csv")
year = df ['year']
continent = df ['continent']
print(year)
print(continent)
print(yearArray)
yearArray = np.array(year)
print(yearArray)
continentArray = np.array(continent)
print(continentArray)
yearContinent = np.array([yearArray,continentArray])
print(yearContinent)
combine = df[["year","continent","lifeExp"]]
print(combine)
