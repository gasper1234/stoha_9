import numpy as np
import matplotlib.pyplot as plt

N = 250
dt = 0.001
N_it = 100000

def prob_dist(N, N_it, dt):
	beta_r = 0.8
	beta_s = 1
	M_1 = np.diag(np.array([1 - (beta_r+beta_s)*i*dt for i in range(2*N)]))
	M_2 = np.diag(np.array([beta_s*i*dt for i in range(1, 2*N)]), k=1)
	M_3 = np.diag(np.array([beta_r*i*dt for i in range(2*N-1)]), k=-1)
	M = M_1 + M_2 + M_3

	x = np.array([0 for _ in range(N-1)]+[1]+[0 for _ in range(N)])
	N_s = np.arange(0, 2*N, 1)

	mom_1 = np.zeros(N_it)
	mom_2 = np.zeros(N_it)
	for i in range(N_it):
		mom_1[i] = np.sum(x*N_s)
		mom_2[i] = np.sum(x*N_s**2)
		x_c = np.copy(x)
		x = M.dot(x_c)
	return mom_1, mom_2

m_1, m_2 = prob_dist(N, N_it, dt)
sigma = np.sqrt(m_2 - m_1**2)
t_it = np.arange(1, N_it+1, 1)/1000
plt.plot(t_it, sigma, label=250)


N = 25
dt = 0.01
N_it = 10000

m_1, m_2 = prob_dist(N, N_it, dt)
sigma = np.sqrt(m_2 - m_1**2)
t_it = np.arange(1, N_it+1, 1)/100
plt.plot(t_it, sigma, label=25)



plt.ylabel(r'$\sigma$')
plt.xlabel(r'$t$')
plt.legend()
plt.show()