import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style

# nekaj za "boljsi slog" a nepotrebno
style.use('fivethirtyeight')

# naredis okno
fig = plt.figure()

# naredis graf v oknu
ax1 = fig.add_subplot(1, 1, 1)

# funkcija, ki se zazene vsak frame
def animate(i):
    # izrabimo numpy da nam pohendla nalaganje tock
    data = np.loadtxt('samplefile.dat')
    
    # zbrises kar je bilo
    ax1.clear()
    # narises na novo
    ax1.plot(data[:, 0], data[:, 1])
        
# z modulom animate za vsak frame pozenes funkcijo animate, narises
# na fig z intervalom 200ms, torej 5x na sekundo
ani = animation.FuncAnimation(fig, animate, interval=200)
# pokazi okno
plt.show()
