import numpy as np
import time

# zgeneriraj sinus
def generate(step):
    elapsed = 0
    while True:
        with open("samplefile.dat", 'a') as f:
            print("{} {}".format(elapsed, np.sin(elapsed)), file=f)
            elapsed += step
        time.sleep(step)
            
generate(0.2)
