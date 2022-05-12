import pandas as pd
import matplotlib.pyplot as plt


data = [['12/31/16', 12.198], ['12/21/17', 12.083], ['12/31/18', 11.968],['12/31/19', 11.979],['12/31/20',11.99],['12/31/21',12.001], ['12/31/22',12.012]]

df = pd.DataFrame(data, columns = ['date', 'births per 1000 people'])

print("Line graph: ")
plt.plot(df["date"], df["births per 1000 people"])
plt.show()

