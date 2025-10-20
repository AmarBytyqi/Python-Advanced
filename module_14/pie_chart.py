import matplotlib.pyplot as plt
import pandas as pd

from module_3.set_methods import colors

df = pd.read_csv("avgIQpercountry.csv")

nobel_prizes_per_continent = df.groupby ('Continent')['Nobel Prices'] .sum()

no_of_continents = nobel_prizes_per_continent.count()

print(no_of_continents)


colors = ['red', 'blue', 'orange', 'gray', 'black', 'green', 'gold', 'purple']

plt.figure(figsize=(10, 6))

nobel_prizes_per_continent.plot(kind="pie", colors=colors, autopct='%1.1f%%')

plt.title('DISTRIBUTION OF NOBEL PRIZES')

plt.xlabel('equal')

plt.ylabel('')

plt.axis()

plt.show()
