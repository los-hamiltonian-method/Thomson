import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

filename = "regulator_680uF.CSV"
df = pd.read_csv(filename).dropna()

fig, ax = plt.subplots()
# Capacitor voltage
Vc = df['capacitor']
# Output voltage close to min and max
Vmid = df['out_mid']
Vmax = df['out_max']

# Plots
ax.scatter(Vc, Vmax, label='Maximum voltage')
ax.scatter(Vc, Vmid, label='Close to minimum voltage')
ax.set(title='Regulator output voltage',
	   xlabel='Capacitor voltage ($V_c$)',
	   ylabel='Ouput voltage ($V$)')

plt.legend()
ax.grid()
plt.show()