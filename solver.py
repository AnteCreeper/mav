import numpy as np
from sklearn.utils import resample


class Solver():
    def __init__(self, list_A: np = None, list_B: np = None, mu=None, SKO=None, n_size_bootstrep=1000):
        if (list_A is None) or (list_B is None):
            start_random_seed = 999
            np.random.seed(start_random_seed)
        if mu is None:
            mu = 382
        persent = 1.002
        if SKO is None:
            SKO = 0.006 * mu
        if list_A is None:
            self.n_size_A = 180
            self.A = np.zeros([self.n_size_A])
            self.A = np.random.normal(mu, SKO, self.n_size_A)
        if list_B is None:
            self.n_size_B = 30
            self.B = np.zeros([self.n_size_B])
            self.B = np.random.normal(persent * mu, SKO, self.n_size_B)
        if list_A is not None:
            self.A = list_A
            self.n_size_A = len(list_A)
        if list_B is not None:
            self.B = list_B
            self.n_size_B = len(list_B)
        self.n_size_bootstrep = n_size_bootstrep

    def get_mean(self):
        return np.mean(self.B[:]) - np.mean(self.A[:])

    def get_bootstrep(self):
        delta = np.zeros([self.n_size_bootstrep])
        average_value_bootstrep_before = np.zeros([self.n_size_bootstrep])
        average_value_bootstrep_after = np.zeros([self.n_size_bootstrep])
        for i in range(self.n_size_bootstrep):
            boot = resample(self.A,
                            replace=True,
                            n_samples=self.n_size_A
                            )
            average_value_bootstrep_before[i] = np.mean(boot[:])
            boot = resample(self.B,
                            replace=True,
                            n_samples=self.n_size_B
                            )
            average_value_bootstrep_after[i] = np.mean(boot[:])
            delta[i] = np.mean(average_value_bootstrep_after) - np.mean(average_value_bootstrep_before)
        return delta

    def get_bootstrep_with_replace(self, n_size_Effect=1000):
        effect = np.zeros([n_size_Effect])
        # A_i = np.zeros([self.n_size_A])  # Объявляем массив
        # B_i = np.zeros([self.n_size_B])  # Объявляем массив
        for i in range(n_size_Effect):
            A_i = resample(self.A, replace=True)
            B_i = resample(self.B, replace=True)
            effect[i] = 100 * (np.mean(B_i) - np.mean(A_i[:])) / np.mean(A_i[:])
        return effect

    def get_delta_critich(self, delta, Alfa):
        print('da2')
        return np.percentile(delta, 100 - Alfa * 100)
