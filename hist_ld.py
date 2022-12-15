import numpy as np
import matplotlib.pyplot as plt

N_it = 10000
N = 25
beta = 1
a = np.random.poisson()
dt = 0.1

def N_death(N_it, beta, dt):
	N_s = np.full(N_it, 0)
	for i in range(N_it):
		N_d = 0
		N = 25
		while N > 0:
			a = np.random.poisson(N*beta*dt)
			N -= a
			N_d += 1
		N_s[i] = N_d*dt
	return N_s

betas = [1, 0.6, 0.3]
for beta in betas:
	for 
	N_d_s = N_death(N_it, beta, dt)
	#print(N_d_s)

	plt.hist(N_d_s, bins=[i for i in range(36)], histtype='step', label=beta)
plt.legend(title=r'$\beta$')
plt.xlabel('t')
plt.ylabel('N')
plt.yticks([500*i for i in range(8)], [500*i/N_it for i in range(8)])
plt.show()