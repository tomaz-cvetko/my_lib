speed = 262.05 #m/s
veter = 12.0 #m/s
g = np.array([0, 0, -9.81]) #m/s^2
ro = 1.16 #kg/m^3 pri 300K 100kPa
m = 20.25 #kg #teze legit topovske krogle
S = 23.44e-3 #m^2 #presek usklajen z legit maso
w = 7.272205e-5 #kotna hitrost zemlje
#w = 1e-3
latitude = 0.7854
#streljamo proti jugu
omega = [-w*math.cos(latitude), 0.0, w*math.sin(latitude)]

def coriolis(y):
    #y = stanje
    #F(v) = F_g + F_{u}(v)
    #F_u = 1/2*\ro*S*(v_rel)^2
    relativna = y[2]- y[1]
    #print relativna

    #C = 0.000001
    C = 0.5*0.47*ro * S * math.sqrt(np.dot(relativna, relativna))
    acc = g + C/m * relativna
    #print acc
    #coriolis: -2*omega x velocity
    cor = -2*np.cross(omega, y[1])

    return acc + cor
