import numpy as np
import matplotlib.pyplot as plt

beta = 0.5 #contamination
N = 10000
T = 100

S0 = 0.999
I0 = 0.001
R0 = 0

S = np.zeros(N)
I = np.zeros(N)
R = np.zeros(N)
t = np.linspace(0, T, N)

dt = T/N

S[0]=S0
I[0]=I0
R[0]=R0

I_g=[]

for gamma in [0.1,0.2,0.3,0.4]:
    for i in range(1,N):
        S[i] = S[i-1] - beta*S[i-1]*I[i-1]*dt
        I[i] = I[i-1] + beta*S[i-1]*I[i-1]*dt - gamma*I[i-1]*dt
        R[i] = R[i-1] + gamma*I[i-1]*dt
    I_g.append(np.array(I))

# Affichage avec matplotlib

# Sans confinement
plt.plot(t, I, '-', label='I(t) sans confinement')

# Pour différentes durées de confinement :
for w in range(len(I_g)):
    plt.plot(t, I_g[w], '--', label='I_c(t), γ = {:.1f}'.format(0.1 + 0.1*w))

plt.title('I(t) pour différentes valeurs de γ')
plt.legend()
plt.grid()
plt.show()