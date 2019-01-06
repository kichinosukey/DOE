import numpy as np

class LHS:
    def __init__(self, n=None, samples=None):
        self.n = n
        self.samples = samples
        self.cut = np.linspace(0, 1, samples+1)
        self.random_state = np.random.RandomState()
        self.u = self.random_state.rand(self.samples, self.n)
        self.a = self.cut[:self.samples]
        self.b = self.cut[1:self.samples+1]
        self.rd = np.zeros_like(self.u)
        self.path1 = []
        self.path2 = []
    
    def sample(self):
        for j in range(self.n):
            self.path1.append(self.u[:, j])
            self.path2.append(self.u[:, j] * (self.b - self.a))
            self.rd[:, j] = self.u[:, j] * (self.b - self.a) + self.a
        
        H = np.zeros_like(self.rd)
        for j in range(self.n):
            order = self.random_state.permutation(range(self.samples))
            H[:, j] = self.rd[order, j]
        return H


