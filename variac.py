import matplotlib.pyplot as plt
import pandas as pd

filename = "variac.txt"
df_variac = pd.read_csv(filename)
print(df_variac)

plt.plot(df_variac['dial#'], df_variac['voltage'])
plt.grid(True)
plt.show()