from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import requests


def get(url):
    raw = requests.get(url).content.decode()
    return np.array(raw.strip().split('\n'), float)

def task1(dist):
    n = len(dist)
    E = np.sum(dist) / n
    D = np.sum((dist-E)**2) / (n-1)
    return {'E': E, 'D': D}

def task2(dist, ncol=10):
    plt.figure(label='Task 2')
    plt.bar_label(plt.hist(dist, ncol)[2])
    plt.show(block=False)

def task3(dtype, E, D):
    if dtype == 'N':
        return E, D
    if dtype == 'E':
        return 1/E, -999
    if dtype == 'U':
        u = (3*D)**.5
        return E-u, E+u

def task4(dist, dtype, E, D, eps=0.05):
    n = len(dist)
    if dtype == 'N':
        return E-stats.t.ppf(1-(eps/2), n-1)*(D/n)**.5, D/stats.chi2.ppf(eps/2, n-1)*(n-1)
    if dtype == 'E':
        return 1/E-stats.norm.ppf(1-eps/2)/n**.5/E, -999
    if dtype == 'U':
        u = stats.norm.ppf(1-eps/2)*(max(dist)-min(dist))/(3*n)**.5
        return 2*E-u-max(dist), 2*E+u-min(dist)

def parse(url):
    dist = get(url)
    args = task1(dist)
    task2(dist)
    dtype = input('dtype = ').upper()
    print('Task 1:', tuple(args.values()))
    print('Task 3:', task3(dtype, **args))
    print('Task 4:', task4(dist, dtype, **args))
