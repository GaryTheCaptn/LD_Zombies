import numpy as np
import matplotlib.pyplot as plt

mu = 0.009 #mortalite et natalite
gamma = 0.1 #remission
beta = 0.4 #contamination
N = 100000
T = 600

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

for i in range(0,N-1):
    S[i+1] = S[i] - beta*S[i]*I[i]*dt + mu*dt - mu*S[i]*dt
    I[i+1] = I[i] + beta*S[i]*I[i]*dt - gamma*I[i]*dt - mu*I[i]*dt
    R[i+1] = R[i] + gamma*I[i]*dt - mu*R[i]*dt


plt.title('S(t), I(t), R(t), β = 0.4, γ = 0.2, µ = 0.009, R0 > 1')
plt.plot(t, S,'-', label='S(t)')
plt.plot(t, I, '-', label='I(t)')
plt.plot(t, R, 'r--', label='R(t)')
plt.legend()
plt.grid()
plt.show()