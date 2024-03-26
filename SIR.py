import numpy as np
import matplotlib.pyplot as plt

def SIR(gamma,beta,S0,I0,R0,dt,seuil):
    S = [S0]
    I = [I0]
    R = [R0]
    i = 1

    while I[-1] >= seuil or i < 20:
        S.append(S[i - 1] - beta * S[i - 1] * I[i - 1] * dt)
        I.append(I[i - 1] + beta * S[i - 1] * I[i - 1] * dt - gamma * I[i - 1] * dt)
        R.append(R[i - 1] + gamma * I[i - 1] * dt)
        i = i+1
    return S, I, R

def affiche_SIR(S,I,R,dt,title):
    plt.title(title)
    taille = len(I)
    t = np.linspace(0,taille*dt,taille)
    plt.plot(t, S, '-', label='S(t)')
    plt.plot(t, I, '-', label='I(t)')
    plt.plot(t, R, 'r--', label='R(t)')
    plt.legend()
    plt.grid()
    plt.show()

# Impact de beta
gamma = 0.1 #rémission
beta_1 = 0.5 #contamination
beta_2 = 0.3
N = 10000
T = 100
dt = T/N
S0 = 0.999
I0 = 0.001
R0 = 0

S,I,R = SIR(gamma,beta_1,S0,I0,R0,dt,0.0005)
affiche_SIR(S,I,R,dt,'S(t), I(t), R(t), β = 0.5, γ = 0.1, seuil = 0.05%')

S,I,R = SIR(gamma,beta_2,S0,I0,R0,dt,0.0005)
affiche_SIR(S,I,R,dt,'S(t), I(t), R(t), β = 0.3, γ = 0.1, seuil = 0.05%')

# Impact d'un confinement
gamma = 0.1 #rémission
beta = 0.35 #contamination hors confinement
beta_c = 0.2 #contamination en confinement
S0 = 0.999
I0 = 0.001
R0 = 0
N = 10000
T = 100
dt = T/N
t1 = [7+5*i for i in range(0,6)] #fin du confinement

def SIR_confinement(gamma,beta,beta_c,S0,I0,dt,seuil,debut_conf):
    S = [S0]
    I = [I0]
    i = 1
    while I[-1] >= seuil or i < 20:
        if i * dt < debut_conf or i * dt > debut_conf+25:
            S.append(S[i - 1] - beta * S[i - 1] * I[i - 1] * dt)
            I.append(I[i - 1] + beta * S[i - 1] * I[i - 1] * dt - gamma * I[i - 1] * dt)
        else:
            S.append(S[i - 1] - beta_c * S[i - 1] * I[i - 1] * dt)
            I.append(I[i - 1] + beta_c * S[i - 1] * I[i - 1] * dt - gamma * I[i - 1] * dt)
        i = i+1
    return S, I

S_sans_conf,I_sans_conf,R_sans_conf = SIR(gamma,beta,S0,I0,R0,dt,0.0005)
taille = len(I_sans_conf)
t = np.linspace(0,taille*dt,taille)
plt.plot(t, I_sans_conf, '-', label='I(t) sans confinement')

for debut_conf in t1:
    Sc, Ic = SIR_confinement(gamma,beta,beta_c,S0,I0,dt,0.0005,debut_conf)
    taille = len(Ic)
    t = np.linspace(0, taille * dt, taille)
    plt.plot(t, Ic, '--', label='I_c(t), t1 = '+str(debut_conf))

plt.title('I(t) avec et sans confinement')
plt.legend()
plt.grid()
plt.show()

# Impact de gamma
beta = 0.5
S0 = 0.999
I0 = 0.001
R0 = 0
N = 10000
T = 100
dt = T/N
for gamma in [0.1,0.2,0.3,0.4]:
    S, I, R = SIR(gamma,beta,S0,I0,R0,dt,0.0005)
    taille = len(I)
    t = np.linspace(0, taille * dt, taille)
    plt.plot(t, I, '--', label='I_c(t), γ = {:.1f}'.format(gamma))
plt.title('I(t) pour différentes valeurs de γ')
plt.legend()
plt.grid()
plt.show()

# Meme R_0 = 1.2 mais differentes valeurs de beta et gamma
dt = T/N
S0 = 0.999
I0 = 0.001
R0 = 0
couples_beta_gamma = [[1/3,0.2],[2/3,0.4],[0.5,0.3],]
I_R0 = []
for couple in couples_beta_gamma:
    beta, gamma = couple[0], couple[1]
    S, I, R = SIR(gamma,beta,S0,I0,R0,dt,0.0005)
    taille = len(I)
    t = np.linspace(0,taille*dt,taille)
    plt.plot(t,I, '--', label=('β = '+str(round(beta,2))+' γ = '+str(round(gamma,2))))
plt.title('I(t) avec R0 = 5/3, seuil = 0.05% et differents couples beta/gamma')
plt.legend()
plt.grid()
plt.show()

# Plan de phase
from phaseportrait import PhasePortrait2D

beta = 0.5
gamma = 0.3
def variations(S,I):
    return - beta*S*I, beta*S*I - gamma*I

SIR_phase = PhasePortrait2D(variations, [[0,1],[0,1]],color='viridis', Title='Plan de phase du modèle SIR', xlabel='Susceptibles', ylabel='Infectés')
fig, ax = SIR_phase.plot()

# Ajouter la diagonale
x_coords = np.linspace(0, 1, 100)
y_coords = 1 - x_coords
ax.plot(x_coords, y_coords, color='black', linestyle='--')  # Tracer la diagonale en rouge en pointillés

fig.show()