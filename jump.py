import numpy as np
from matplotlib import pyplot as plt
import sys


class Jump():
    """"This class analyzes plyometric jump data for; squat, countermovement, and drop jumps."""
    def __init__(self, filename):
        with open(filename) as infile:
            temp = infile.readline()  # skip first line
            temp = infile.readline()
            header = temp.split(',')
            self.n = int(header[9])
            self.samplingrate = float(header[10])
            self.mass = float(header[11])
        data_load = np.loadtxt(filename, skiprows=2, delimiter=",")
        self.t = data_load[:, 0]
        self.fz = data_load[:, 1]

    def plot_force(self):
        plt.title("Squat Jump")
        plt.ylabel("Vertical Force (N)")
        plt.xlabel("Time (s)")
        plt.plot(self.t, self.fz)
        plt.show()
