import scipy.integrate as integrate
import numpy as np
import math as m


def old():
    """Old attempt at this"""
    therm = [[300.], [300.], [300.], [300.], [300.], [300.], [300.], [300.], [300.], [300.]]
    ts = np.linspace(0, 50, 1000)

    #odvod temperature bo vsota gradientov (diferencialov) z desne in z leve glede x
    #dT/dt[i] = K/x^2 * (temperature[i-1]- 2*temperature[i] + temperature[i+1])
    #razen ce je robna tocka
    #potem je treba nekaj scarat - robna bo funkcija
    def odvod(indeks, arr, K, time):
        odvodt = K * (arr[indeks-1][time] - 2*arr[indeks][time] + arr[indeks+1][time])
        return odvodt

    def robna(time):
        return 5*m.cos(0.05*time)


    K = 0.02
    x = 0.003

    def main_old():
        t = 0
        dt = 50. / 1000.
        for time in ts:
            for i in range(0,9):
                therm[i].append(therm[i][t] + (robna(time) if i==0 else  odvod(i, therm, K, t)*dt/(x**2)))
            therm[9].append(300.)
            t+=1

        import matplotlib.pyplot as plt

        plt.plot(ts[:], therm[4][:-1], label = 'T(t)')
        plt.show()
        
    main_old()
    
class Bloki(object):
    def __init__(self, n, temperature, koeficient_prevodnosti, kapaciteta, levi_rob, desni_rob):
        self.progress = 0
        self.n = n
        self.default_temperature = temperature
        self.senzorji = [[temperature] for i in range(n)]
        
        self.levi = levi_rob
        self.desni = desni_rob
        
        self.senzorji[0][0] = self.levi(0)
        self.senzorji[-1][0] = self.desni(0)
        
        self.K = koeficient_prevodnosti
        self.kapaciteta = kapaciteta
        
    def temperaturne_razlike(self):
        def bilancaT(i):
            return self.senzorji[i-1][self.progress] - 2*self.senzorji[i][self.progress] + self.senzorji[i+1][self.progress]
        r = [bilancaT(i) for i in range(1, self.n - 1)]
        return r
        
    def __call__(self, cas, delta_t):
        self.senzorji[0].append(self.levi(cas))
        
        dTs = self.temperaturne_razlike()
        
        for i in range(1, self.n-1):
            dQ = delta_t * (self.K *dTs[i-1])
            self.senzorji[i].append(self.senzorji[i][self.progress] + dQ/self.kapaciteta)
            
        self.senzorji[-1].append(self.desni(cas))
        
        self.progress += 1
        
    def getData(self, indeks):
        return self.senzorji[indeks][:]
    
    def getSlice(self, point):
        return [senzor[point] for senzor in self.senzorji]
        
        
   
T_0 = 300.0
   
def robni_grelec(cas):
    """Sinusni potek temperature, s periodo 50s in amplitudo 10K"""
    return 300.0 + 10*m.sin(m.pi/50 * cas)

def robna_stena(temperature):
    """Vrne funkcijo, ki bo vracala zeljeno konstanto"""
    return lambda cas : temperature
    
def main():
    print("starting the right main")
    prevodnost = 0.1  # podatki o blokih
    debelina = 0.03
    stena = robna_stena(290.0)  # funkcija za vracanje konstantne vrednosti
    c = 800
    koeficient = prevodnost/debelina  # dQ = koeficient * dT
    
    merjenec = Bloki(100, 300.0, koeficient, 1, robni_grelec, stena)
    
    import matplotlib.pyplot as plt
    
    t_limit = 120
    t = 0
    dt = 0.1
    casovna_os = [t]
    
    
    plt.ion()
    plt.figure()
    
    while t < t_limit:
        merjenec(t, dt)
        t += dt
        casovna_os.append(t)
    
    i = 0
    for cas in casovna_os:
        temp = merjenec.getSlice(i)
        plt.clf()
        plt.plot(range(0, len(temp)), temp, label=cas)
        plt.xlabel("Location")
        plt.ylabel("Temperature")
        plt.legend()
        plt.grid(True)
        plt.pause(0.01)
        
        i += 1
        
        
    from matplotlib import pyplot as plt
    #data = merjenec.getData(0)
    #plt.plot(casovna_os, data, 'r-', label='sine')
    #data = merjenec.getData(2)
    #plt.plot(casovna_os, data, 'g-', label='third')
    #data = merjenec.getData(3)
    #plt.plot(casovna_os, data, 'b-', label='fourth')
    
    #for i in range(0, 100, 10):
        #data = merjenec.getSlice(i)
        #plt.plot(range(0, len(data)), data)
    
    #data = merjenec.getSlice(100)
    #plt.plot(range(0, len(data)), data, label='slice100')
    #data = merjenec.getSlice(-1)
    #plt.plot(range(0, len(data)), data, label='slice12000')
    #data = merjenec.getSlice(6000)
    #plt.plot(range(0, len(data)), data, label='slice6000')
    
    #plt.legend()
    
    #plt.show()
    
    
if __name__ == "__main__":
    main()
