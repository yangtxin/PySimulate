import matplotlib.pyplot as plt
import numpy as np
n = 4000000
rn = 0.1
at = 0
tsn = 0.5
A = 0.05
B = 0.5
delta_t = 0.001
#%%
rnArray = np.zeros(n)
ytsnArray = np.zeros(n)
delta_rnArray = np. zeros(n)
for i in range(n):
    if i < 600000:
        tsn = 0.5
    else:
        tsn = 0.0
    at = at + delta_t - at * np.tanh(1000 * tsn)
    ytsn = ((np.tanh(1000000 * (at - A)) + 1) * 10000 + 1) * (rn + 1) - 1
    ydeltat = ((np.tanh(-1000000*(at-B))+1) * 10000 + 1) * (10 * np.e ** (-0.1 * rn) + 1) - 1
    delta_mn = (np.e ** (-ytsn) - np.e ** (-ydeltat)) * delta_t
    rn = rn + delta_mn

    delta_rnArray[i] = delta_mn
    ytsnArray[i] = ytsn
    rnArray[i] = rn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    plt.figure('delta_rnArray')
    plt.plot(delta_rnArray)
    plt.grid()

    plt.figure('ytsnArray')
    plt.plot(ytsnArray)
    plt.grid()

    plt.figure('rnArray')
    plt.plot(rnArray)
    plt.grid()

    plt.show()
