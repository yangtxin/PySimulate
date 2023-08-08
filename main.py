# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
n = 4000000
mn = 0.1
rn = 0
at = 0
tre = 0.5
A = 0.05
B = 0.5
at = 0
delta_t = 0.001
#%%
mnArray = np.zeros(n)
ytreArray = np.zeros(n)
delta_mnArray = np. zeros(n)
for i in range(n):
    if i < 600000:
        tre = 0.5
    else:
        tre = 0.0
    at = at + delta_t - at * np.tanh(1000 * tre)
    ytre = ((np.tanh(1000000 * (at-A)) + 1) * 10000 + 1) * (mn+1)-1
    ydeltat = ((np.tanh(-1000000*(at-B))+1) * 10000 + 1) * (10*np.e**(-0.1*mn)+1)-1
    # ydeltat = ((np.tanh(-1000000*(at-B))+1) * 10000 + 1) * (25*np.tanh(-rn)+1)-1
    delta_mn = (np.e**(-ytre) - np.e**(-ydeltat)) * delta_t
    mn = mn + delta_mn

    delta_mnArray[i] = delta_mn
    ytreArray[i] = ytre
    mnArray[i] = mn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    plt.figure('delta_rnArray')
    plt.plot(delta_mnArray)
    plt.grid()

    plt.figure('ytsnArray')
    plt.plot(ytreArray)
    plt.grid()

    plt.figure('rnArray')
    plt.plot(mnArray)
    plt.grid()

    plt.show()

