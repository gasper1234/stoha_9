import numpy as np
import matplotlib.pyplot as plt

N_it = 1000
N = 250
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
t_s = [0.02*i for i in range(1, 100)]
for beta in betas:
	t_d_s = []
	for dt in t_s:
		print(dt)
		N_d_s = N_death(N_it, beta, dt)
		t_d = np.average(N_d_s)
		t_d_s.append(t_d)
	#print(N_d_s)

	plt.plot(t_s, t_d_s, 'x', label=beta)
plt.legend(title=r'$\beta$')
plt.xlabel('dt')
plt.ylabel(r'$t_{ex}$')
plt.show()