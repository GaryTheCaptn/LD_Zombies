from matplotlib import pyplot
import numpy as np

from phaseportrait import PhasePortrait3D

mu = 0.009 #mortalite et natalite
gamma = 0.1 #remission
beta = 0.4 #contamination
alpha = 0.3 #incubation

def variations(S,E,I):
    return mu - mu*S - beta*S*I, beta*S*I - alpha*E, alpha*E - gamma*I - mu*I

SIR_phase = PhasePortrait3D(variations, Range=[[0,1],[0,1],[0,1]], color='viridis', Title='Plan de phase SEIR(D) β=0.3, α=0.3, γ=0.1, µ=0.009', xlabel='Susceptibles', ylabel='Exposés',zlabel='Infectés')
fig, ax = SIR_phase.plot()
fig.show()