from matplotlib import pyplot
import numpy as np

from phaseportrait import PhasePortrait2D

beta = 0.4
gamma = 0.5

def variations(S,I):
    return - beta*S*I, beta*S*I - gamma*I

SIR_phase = PhasePortrait2D(variations, [[0,1],[0,1]],color='viridis', Title='Plan de phase du modèle SIR', xlabel='Susceptibles', ylabel='Infectés')
fig, ax = SIR_phase.plot()

# Ajouter la diagonale
x_coords = np.linspace(0, 1, 100)
y_coords = 1 - x_coords

ax.plot(x_coords, y_coords, color='black', linestyle='--')  # Tracer la diagonale en rouge en pointillés


fig.show()