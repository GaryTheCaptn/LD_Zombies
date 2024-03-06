import numpy as np
import matplotlib.pyplot as plt

gamma = 0.1 #rémission
beta_1 = 0.5 #contamination
beta_2 = 0.3
N = 10000
T = 100

S0 = 0.999
I0 = 0.001
R0 = 0

# Premiere modelisation avec beta = 0.5
S = np.zeros(N)
I = np.zeros(N)
R = np.zeros(N)
t = np.linspace(0, T, N)

dt = T/N

S[0]=S0
I[0]=I0
R[0]=R0

for i in range(1,N):
    S[i] = S[i-1] - beta_1*S[i-1]*I[i-1]*dt
    I[i] = I[i-1] + beta_1*S[i-1]*I[i-1]*dt - gamma*I[i-1]*dt
    R[i] = R[i-1] + gamma*I[i-1]*dt


plt.title('S(t), I(t), R(t), β = 0.5, γ = 0.1')
plt.plot(t, S,'-', label='S(t)')
plt.plot(t, I, '-', label='I(t)')
plt.plot(t, R, 'r--', label='R(t)')
plt.legend()
plt.grid()
plt.show()

# Premiere modelisation avec beta = 0.3
S = np.zeros(N)
I = np.zeros(N)
R = np.zeros(N)
t = np.linspace(0, T, N)

dt = T/N

S[0]=S0
I[0]=I0
R[0]=R0

for i in range(1,N):
    S[i] = S[i-1] - beta_2*S[i-1]*I[i-1]*dt
    I[i] = I[i-1] + beta_2*S[i-1]*I[i-1]*dt - gamma*I[i-1]*dt
    R[i] = R[i-1] + gamma*I[i-1]*dt


plt.title('S(t), I(t), R(t), β = 0.3, γ = 0.1')
plt.plot(t, S,'-', label='S(t)')
plt.plot(t, I, '-', label='I(t)')
plt.plot(t, R, 'r--', label='R(t)')
plt.legend()
plt.grid()

plt.show()
plt.plot(S,I)
plt.show()