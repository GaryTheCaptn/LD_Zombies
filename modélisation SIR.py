import numpy as np
import matplotlib.pyplot as plt

gamma = 0.1 #rémission
beta = 0.35 #contamination
beta_c = 0.2 #contamination en confinement
t1 = 7 #début du confinement
t2 = t1+25 #fin du confinement
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

for i in range(1,N):
    S[i] = S[i-1] - beta*S[i-1]*I[i-1]*dt
    I[i] = I[i-1] + beta*S[i-1]*I[i-1]*dt - gamma*I[i-1]*dt
    R[i] = R[i-1] + gamma*I[i-1]*dt


plt.title('S(t), I(t), R(t)')
plt.plot(t, S,'-', label='S(t)')
plt.plot(t, I, '+', label='I(t)')
plt.plot(t, R, 'r--', label='R(t)')
plt.legend()
plt.grid()
plt.show()

plt.plot(S,I)
plt.show()

S_c = np.zeros(N)
I_c = np.zeros(N)
R_c = np.zeros(N)

S_c[0]=S0
I_c[0]=I0
R_c[0]=R0



t1_1 = t1
I_cc=[]
for v in range(6):
    for i in range(1, N):
        if i * dt < t1_1 or i * dt > (t1_1+25):
            S_c[i] = S_c[i - 1] - beta * S_c[i - 1] * I_c[i - 1] * dt
            I_c[i] = I_c[i - 1] + beta * S_c[i - 1] * I_c[i - 1] * dt - gamma * I_c[i - 1] * dt
        else:
            S_c[i] = S_c[i - 1] - beta_c * S_c[i - 1] * I_c[i - 1] * dt
            I_c[i] = I_c[i - 1] + beta_c * S_c[i - 1] * I_c[i - 1] * dt - gamma * I_c[i - 1] * dt
    I_cc.append(np.array(I_c))
    t1_1+=5

plt.title('I(t) avec et sans confinement')
plt.plot(t, I, '-', label='I(t) sans confinement')
for w in range(len(I_cc)):
    plt.plot(t, I_cc[w], '--', label='I_c(t), t1 = {}'.format(t1 + 5*w))
plt.legend()
plt.grid()
plt.show()
