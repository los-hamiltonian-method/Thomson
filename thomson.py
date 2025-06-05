'''Calculates parameter range for Thomson experiment.'''
import numpy as np
import itertools as it
import matplotlib.pyplot as plt

q = 1.6e-19 # C
m = 9.1e-31 # kg
V_cat = [1000, 1500] # V, a 2kV se calienta mucho
phi = [6.57e-19, 8.17e-19] # J, work function range for common metals.
mu = 4 * np.pi * 10**(-7) # N/A

def calculate_I(vel_cat: list, Rb_Rt: list):
	'''Calculates current intensity range.'''
	I_s = []
	denominator = mu * q
	for v in vel_cat:
		for r in Rb_Rt:
			numerator = np.sqrt(8) * m * v
			I = numerator * r / denominator
			I_s.append(I)
	return I_s


def calculate_vel_cat(V_cat: list, phi: list):
	phi_V_cat = []
	for V in V_cat:
		for p in phi:
			phi_V_cat.append(np.sqrt(2*(e*V - p)/m))
	return phi_V_cat


def extract_minmax(A: list):
	return np.linspace(min(A), max(A), 2)

Rb_Rt = [1, 3]
vel_cat = calculate_vel_cat(V_cat, phi)
vel_cat = extract_minmax(vel_cat)
print(f'Vel. cat. range: {vel_cat}')

I_s = calculate_I(vel_cat, Rb_Rt)
I_s = extract_minmax(I_s)
print(f'Velocity range: {vel_cat}')
print(f'Current range: {I_s}')
