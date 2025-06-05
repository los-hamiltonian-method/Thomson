import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

filename_os = "rectifier_680uF_min_max.txt"
df_os = pd.read_csv(filename_os)
AC = df_os['AC']
DC = df_os['DC_min']

# Fits
f = lambda x, a, b: a*x + b
fit = curve_fit(f, AC, DC)
a, b = fit[0][0], fit[0][1]
print(f"{a = }, {b = }")

# Plots
x = np.linspace(np.min(AC), np.max(AC), 100)
y = a*x + b
fig, ax = plt.subplots()
ax.scatter(AC, DC)
ax.plot(x, f(x, a, b))
ax.set(title="AC vs 680uF DC", xlabel="AC", ylabel="DC")
ax.grid(True)
plt.show()