import numpy as np
import matplotlib.pyplot as plt

N = 25
beta = 1
a = np.random.poisson()
dt = 0.1
grid = np.zeros((N+1, 60))

for _ in range(200):
	N_s = np.full(60, 0)
	ind = 0
	N = 25
	while N > 0:
		a = np.random.poisson(N*beta*dt)
		N -= a
		ind += 1
		if ind >= 60:
			break
		if N > 0:
			N_s[ind] = N
	for i in range(1, len(N_s)):
		grid[N_s[i], i] += 1
		if N_s[i] == 0:
			break

grid_1 = np.flip(grid, 0)
plt.imshow(grid_1, cmap='Greys')
plt.yticks([5*i for i in range(6)], [str(-5*(i-5)) for i in range(6)])

plt.xlabel('t')
plt.ylabel('N')
plt.show()