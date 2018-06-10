from matplotlib import pyplot as plt
import numpy as np

def ciexp(phi):
    return np.array((np.cos(phi), np.sin(phi)))


Omega = 1.9
freq0 = 2.0

def main():
    time = np.linspace(2, 100, 30000)
    a = np.transpose(ciexp((-Omega - freq0)*time))
    b = np.transpose(ciexp((-Omega + freq0)*time))

    gibanje = 2*a-3*b

    plt.plot(gibanje[:, 0], gibanje[:, 1], 'b-')
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    main()