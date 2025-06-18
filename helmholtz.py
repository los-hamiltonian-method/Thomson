import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

@np.vectorize
def transverse_field_z(r0, a, d):
	'''
	Returns z-field strength for a pair of
	coils at z = 0,  r0. (I mu_0 / 4 pi = 1)
	Parameters
	----------
	r0: float
		Perpendicular distance from coils axis.
	a: float
		Coils radius.
	d: float
		Coils separation distance.
	'''
	b = d / 2
	integrand = lambda theta, r0, a, b: a * (a -  r0 * np.cos(theta)) / (a**2 + b**2 + r0**2 - 2 * a * r0 * np.cos(theta))**(3/2)
	return quad(integrand, 0, 2 * np.pi, args=(r0, a, b))[0]


@np.vectorize
def transverse_field_r(r0, a, d):
	'''
	Returns r-field strength for a pair of
	coils at z = 0,  r0. (I mu_0 / 4 pi = 1)
	Parameters
	----------
	r0: float
		Perpendicular distance from coils axis.
	a: float
		Coils radius.
	d: float
		Coils separation distance.
	'''
	b = d / 2
	integrand = lambda theta, r0, a, b: -a * b / (a**2 + b**2 + r0**2 - 2 * a * r0 * np.cos(theta))**(3/2)
	return quad(integrand, 0, 2 * np.pi, args=(r0, a, b))[0]


@np.vectorize
def axial_field_z(z, a, d):
	b = d / 2
	return (a**2 / 2) * (1 / (a**2 + (z - b)**2)**(3/2) + 1 / (a**2 + (z + b)**2)**(3/2))


def graph():
	fig, axs = plt.subplot_mosaic([['t_z', 't_r', 'v_z']])
	a = 1
	d = 1
	r = np.linspace(-2 * a, 2 * a, 1000)
	z = np.linspace(-2 * d, 2 * d, 1000)

	ax_variables = [r, r, z]
	ax_functions = [transverse_field_z, transverse_field_r, axial_field_z]
	ax_xlabels = ["Separation from coil axis $r$", "Separation from coil axis ($r$)",
				  "Height from transverse plane ($z$)"]
	ax_titles = ["Transverse field $B_z$", "Transverse field $B_r$", "Axial field $B_z"]

	for name, function, xlabel, title in zip(axs, ax_functions, ax_xlabels, ax_titles):
		axs[name].plot(r, function(r, a, d), label="Field strength")
		axs[name].axvline(a, ls='--', color='k',	 label=f'Radius ${a = }$')
		axs[name].axvline(-a, ls='--', color='k', label=f'Radius ${a = }$')
		axs[name].grid(True, ls='--', color='#ccc')
		axs[name].set(title=title, xlabel=xlabel, ylabel='Field intensity ($B$)')
		plt.legend()
	
	plt.subplots_adjust(hspace=0.5, wspace=0.5)
	plt.show()

graph()


