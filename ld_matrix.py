import numpy as np
import matplotlib.pyplot as plt

N = 250
a = np.random.poisson()
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
	N_s = np.arange(0, N, 1)

	t_s = np.zeros(N_it)
	for i in range(N_it):
		x_c = np.copy(x)
		x = M.dot(x_c)
		t_s[i] = x[0]-x_c[0]
	return t_s

t_s = prob_dist(N, N_it, dt)

# t_s določa povprečja, spremeni v funkxcijo
# poračunaj še za 25 folka


print('pov', np.sum(t_s*np.arange(1, N_it+1, 1)))
print(t_s*np.arange(1, N_it+1, 1))
plt.plot(np.arange(1, N_it+1, 1)/1000, t_s*1000)
plt.ylabel('delež')
plt.xlabel(r'$t_d$')
plt.show()
