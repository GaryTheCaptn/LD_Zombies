import numpy as np
import matplotlib.pyplot as plt

mu = 0.009 #mortalite et natalite
gamma = 0.1 #remission
beta = 0.4 #contamination
alpha = 0.3 #incubation
N = 100000
T = 700

S0 = 0.999
E0 = 0.0005
I0 = 0.0005
R0 = 0

S = np.zeros(N)
E = np.zeros(N)
I = np.zeros(N)
R = np.zeros(N)
t = np.linspace(0, T, N)

dt = T/N

S[0]=S0
E[0]=E0
I[0]=I0
R[0]=R0

for i in range(0,N-1):
    S[i+1] = S[i] - beta*S[i]*I[i]*dt + mu*dt - mu*S[i]*dt
    E[i+1] = E[i] + beta*S[i]*I[i]*dt - alpha*E[i]*dt - mu*E[i]*dt
    I[i+1] = I[i] + alpha*E[i]*dt - gamma*I[i]*dt - mu*I[i]*dt
    R[i+1] = R[i] + gamma*I[i]*dt - mu*R[i]*dt


plt.title('S(t), I(t), R(t), β = 0.4, α = 0.3, γ = 0.1, µ = 0.009, R0 > 1')
plt.plot(t, S,'-', label='S(t)')
plt.plot(t, E,'-', label='E(t)')
plt.plot(t, I, '-', label='I(t)')
plt.plot(t, R, 'r--', label='R(t)')
plt.legend()
plt.grid()
plt.show()