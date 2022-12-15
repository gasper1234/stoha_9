import numpy as np
import matplotlib.pyplot as plt
from numba import njit

Z_0 = 200
L_0 = 50

@njit
def step(Z, L, Z_0, L_0):
	alpha = 1
	beta = 1
	dt = 0.01
	dz = np.random.poisson(Z*5*alpha*dt) - np.random.poisson(Z*4*alpha*dt) - np.random.poisson(Z*L/L_0*alpha*dt)
	dl = np.random.poisson(L*4*beta*dt) - np.random.poisson(L*5*beta*dt) + np.random.poisson(Z*L/Z_0*beta*dt)
	return Z+dz, L+dl


N_it = 20000
@njit
def t_d_dist(N_it):
	t_d_s = np.zeros(N_it)
	for j in range(N_it):
		N_max = 100000
		#Z_s = np.zeros(N_max)
		#L_s = np.zeros(N_max)
		#Z_s[0] = Z_0
		#L_s[0] = L_0
		L = L_0
		Z = Z_0
		for i in range(N_max-1):
			Z, L = step(Z, L, Z_0, L_0)
			if Z <= 0 or L <= 0:
				plot_ind = i
				t_d_s[j] = i
				break
	return t_d_s

t_d_s = t_d_dist(N_it)/100
print(np.average(t_d_s))
	#plt.plot(Z_s[:plot_ind], L_s[:plot_ind])
#print(t_d_s)
plt.hist(t_d_s, bins=[i for i in range(70)])
plt.xlabel(r'$t_d$')
plt.ylabel(r'$N/N_0$')
plt.yticks([i*200 for i in range(9)], [i*200/N_it for i in range(9)])
plt.show()

