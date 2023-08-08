import matplotlib.pyplot as plt
import numpy as np

n = 1000000

tn = 0
deltaT = 0.001

tnArray = np. zeros(n)
for i in range(n):
    deltaTn = np.e**(-tn)*deltaT*1000

    tn = tn + deltaTn

    tnArray[i] = tn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    plt.figure('tnArray*0.001')
    plt.plot(tnArray)
    plt.grid()

    plt.show()
