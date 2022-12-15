import numpy as np
import matplotlib.pyplot as plt
from numba import njit

D_0 = 990
B_0 = 10
gamma = 0.006

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
	#print(-d_Z + d_I)
	#print(d_Z - d_B)
	#print(d_B - d_I)
	return D, B, I


N_it = 400
@njit
def t_d_dist(N_it, D_0, B_0, gamma):
	D_s = np.zeros(N_it)
	B_s = np.zeros(N_it)
	I_s = np.zeros(N_it)
	D_s[0] = D_0
	B_s[0] = B_0
	I_s[0] = 0
	ind = N_it
	for i in range(N_it-1):
			D, B, I = step(D_s[i], B_s[i], I_s[i], gamma)
			if B <= 0:
				print('b', B)
				ind = i
				break
			D_s[i+1], B_s[i+1], I_s[i+1] = D, B, I
	return D_s, B_s, I_s, ind

D, B, I, ind = t_d_dist(N_it, D_0, B_0, gamma)
print('ind', ind)
print(I)
t = np.arange(0, ind, 1)
plt.plot(t,B[:ind], label='bolni')
plt.plot(t,D[:ind], label='zdravi')
plt.plot(t,I[:ind], label='imuni')
plt.legend()
plt.xlabel('t')
plt.ylabel('N')
plt.show()