import numpy as np
import matplotlib.pyplot as plt
from numba import njit

D_0 = 990
B_0 = 10
gamma = 0.003

@njit
def step(D, B, I, gamma):
	N = 1000
	alpha = 0.3
	beta = 0.1
	dt = 1
	d_Z = np.random.poisson(alpha*D/N*B*dt)
	d_I = np.random.poisson(gamma*I*dt)
	d_B = np.random.poisson(beta*B*dt)
	D += -d_Z + d_I
	B += d_Z - d_B
	I += d_B - d_I
	return D, B, I


N_it = 10000
@njit
def t_d_dist(N_it, D_0, B_0, gamma):
	t_e_s = np.zeros(N_it)
	for j in range(N_it):
		D = D_0
		B = B_0
		I = 0
		for i in range(100000):
				D, B, I = step(D, B, I, gamma)
				if B <= 0:
					t_e_s[j] = i
					break
		if t_e_s[j] == 0:
			print('ni ok')
	return t_e_s

gamma_s = [0.0001*i for i in range(40)]
ave_s = []
std_s = []
fig, ax = plt.subplots(2, sharex=True)
for gamma in gamma_s:
	t_e_s = t_d_dist(N_it, D_0, B_0, gamma)
	ave_s.append(np.average(t_e_s))
	std_s.append(np.max(t_e_s))
	#plt.hist(t_e_s, bins=[i*2 for i in range(300)], histtype='step', label=gamma)

ax[0].plot(gamma_s, ave_s, 'x')
ax[1].plot(gamma_s, std_s, 'x')
ax[0].set_ylabel(r'$t_{ave}$')
ax[1].set_ylabel(r'$\sigma$')
ax[1].set_xlabel(r'$\gamma$')
'''
plt.xlabel(r'$t_d$')
plt.ylabel(r'$N/N_0$')
plt.yticks([i*50 for i in range(9)], [i*50/N_it for i in range(9)])
plt.legend(title=r'$\gamma$')
'''
plt.show()