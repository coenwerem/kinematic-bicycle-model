import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

        
class Bicycle(Bicycle):
    def step(self, v, w):
        # ==================================
        #  Kinematic model implementation
        # ==================================
        for self.sample_time in range(0, 100, 0.01):
            self.delta = self.delta +  (w*self.sample_time) 
            self.theta = self.theta + ((v*np.cos(self.beta)*np.tan(self.delta))/self.L)*self.sample_time
            self.xc = self.xc + (v*np.cos(self.theta + self.beta))*self.sample_time
            self.yc = self.yc + (v*np.sin(self.theta + self.beta))*self.sample_time
            self.sample_time += self.sample_time
            if w > self.w_max:
                break
        
        self.beta = np.arctan((self.lr*np.tan(self.delta))/self.L)
         
        pass