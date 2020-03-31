import matplotlib.pyplot as plt

time = []
Vabs = []
dist = []

with open('stat.txt') as f:
    for line in f.readlines():
        *other, t, v, d = line.strip().split(',')
        time.append(float(t))
        Vabs.append(float(v))
        dist.append(float(d))

fig, axs = plt.subplots(3, gridspec_kw={'hspace': 0.5})
axs[0].plot(time, Vabs, '-o')
axs[0].set(xlabel='time', ylabel='Vabs')

axs[1].plot(time, dist, '-o')
axs[1].set(xlabel='time', ylabel='dist')

axs[2].plot(dist, Vabs, 'o')
axs[2].set(xlabel='dist', ylabel='Vabs')

plt.show()
