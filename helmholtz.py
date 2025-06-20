import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

@np.vectorize
def transverse_field_z(r, a, d):
	'''
	Returns z-field strength for a pair of
	coils at z = 0,  r. (I mu_0 / 4 pi = 1)
	Parameters
	----------
	r: float
		Perpendicular distance from coils axis.
	a: float
		Coils radius.
	d: float
		Coils separation distance.
	'''
	b = d / 2
	integrand = lambda theta, r, a, b: a * (a -  r * np.cos(theta)) / (a**2 + b**2 + r**2 - 2 * a * r * np.cos(theta))**(3/2)
	return quad(integrand, 0, 2 * np.pi, args=(r, a, b))[0]


@np.vectorize
def transverse_field_r(r, a, d):
	'''
	Returns r-field strength for a pair of
	coils at z = 0,  r. (I mu_0 / 4 pi = 1)
	Parameters
	----------
	r: float
		Perpendicular distance from coils axis.
	a: float
		Coils radius.
	d: float
		Coils separation distance.
	'''
	b = d / 2
	integrand = lambda theta, r, a, b: -a * b / (a**2 + b**2 + r**2 - 2 * a * r * np.cos(theta))**(3/2)
	return quad(integrand, 0, 2 * np.pi, args=(r, a, b))[0]


@np.vectorize
def axial_field_z(z, a, d):
	'''
	Returns z-field strength for a pair of
	coils at r = 0,  z. (I mu_0 / 4 pi = 1)
	Parameters
	----------
	r: float
		Perpendicular distance from coils axis.
	a: float
		Coils radius.
	d: float
		Coils separation distance.
	'''
	b = d / 2
	return (a**2 / 2) * (1 / (a**2 + (z - b)**2)**(3/2) + 1 / (a**2 + (z + b)**2)**(3/2))


def graph():
	# Format
	rcParams = {'font.family': 'Times New Roman', 'mathtext.fontset': 'cm'}
	plt.rcParams.update(rcParams)

	a = 1
	d = 1
	r = np.linspace(-2 * a, 2 * a, 1000)
	z = np.linspace(-2 * d, 2 * d, 1000)

	# Plotting
	fig, axs = plt.subplot_mosaic([['t_z', 't_r', 'v_z']], figsize=(16, 9))
	fig.suptitle("Normalized magnetic fields for a pair of coaxial coils")
	ax_variables = [r, r, z]
	ax_parameters = [a, a, d / 2]
	ax_functions = [transverse_field_z, transverse_field_r, axial_field_z]
	ax_xlabels = ["Separation from coil axis ($r$)",
				  "Separation from coil axis ($r$)",
				  "Height from transverse plane ($z$)"]
	ax_labels = [f"Radius ${a  = }$", f"Radius ${a  = }$",
				 f"Axial half-separation ${d / 2  = }$"]
	ax_titles = ["Transverse field $B_z$", "Transverse field $-B_r$",
				 "Axial field $B_z$"]

	# Unifromity threshold
	threshold = 0.9
	ax_zip = zip(axs, ax_functions, ax_variables, ax_titles, ax_xlabels,
				 ax_labels, ax_parameters)
	for name, function, variable, title, xlabel, label, param in ax_zip:
		# Strength at 0 and normalization
		B = function(variable, a, d)
		B0 = (function(0, a, d) - np.min(B)) / (np.max(B) - np.min(B))
		B = (B - np.min(B)) / (np.max(B) - np.min(B))
		variable = variable[B <= B0]
		B = B[B <= B0]

		# Distance at which field strength falls to a value < threshold * B(0)
		max_distance = np.min(np.abs(variable[B < threshold * B0]))

		# Plots and format
		axs[name].plot(variable, B, label="Field strength")
		axs[name].axvline(param, ls='--', color='k', label=label)
		axs[name].axvline(-param, ls='--', color='k')
		axs[name].axvline(max_distance, ls='--', color='r',
						  label=f"$B \\geq {threshold} B(0)$ at "
						  		f"$\\leq {max_distance:.2f}$")
		axs[name].axvline(-max_distance, ls='--', color='r')
		axs[name].grid(True, ls='--', color='#ccc')
		axs[name].set(title=title, xlabel=xlabel, ylabel='Field intensity ($B$)')
		axs[name].legend(loc='lower center')

	plt.subplots_adjust(hspace=0.5, wspace=0.3)
	plt.savefig(f"Figures/coils_field_uniformity_{threshold}.pdf")
	plt.savefig(f"Figures/coils_field_uniformity_{threshold}.png", dpi=300)
	plt.show()

graph()
