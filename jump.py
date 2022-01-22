import numpy as np
from matplotlib import pyplot as plt


class Jump():
    """"This class analyzes plyometric jump data for; squat, countermovement, and drop jumps.
    Jump(path with filename, jump type)
    jump type 0 for sj, 1 for cmj, 2 for dj"""
    def __init__(self, filename, jt):
        if jt == 0:
            self.JumpType = "Squat Jump"
        elif jt == 1:
            self.JumpType = "Countermovement Jump"
        else:
            self.JumpType = "Drop Jump"
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
        plt.title(self.JumpType)
        plt.ylabel("Vertical Force (N)")
        plt.xlabel("Time (s)")
        plt.plot(self.t, self.fz)
        plt.show()
