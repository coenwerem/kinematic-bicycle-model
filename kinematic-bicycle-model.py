import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Initializing Bicycle model class and defining reset function (with zero initial conditions)
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
        # Kinematic Bicycle model implementation (with numerical integration to propagate the kinematics through time)
        # Implementation below is for every time step
        # ==================================
        self.delta = self.delta +  (w*self.sample_time)
        self.theta = self.theta + ((v*np.cos(self.beta)*np.tan(self.delta))/self.L)*self.sample_time
        self.xc = self.xc + (v*np.cos(self.theta + self.beta))*self.sample_time
        self.yc = self.yc + (v*np.sin(self.theta + self.beta))*self.sample_time
        
            
        self.beta = np.arctan((self.lr*np.tan(self.delta))/self.L)
         
        pass

sample_time = 0.01
time_end = 20
model = Bicycle()
##solution_model = BicycleSolution()
# set delta directly
model.delta = np.arctan(2/10)
##solution_model.delta = np.arctan(2/10)
t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)

##x_solution = np.zeros_like(t_data)
##y_solution = np.zeros_like(t_data)

for i in range(t_data.shape[0]):
    x_data[i] = model.xc
    y_data[i] = model.yc
    model.step(np.pi, 0)
##x_solution[i] = solution_model.xc
##y_solution[i] = solution_model.yc
##solution_model.step(np.pi, 0)
    
model.beta = 0
#solution_model.beta=0

plt.axis('equal')
plt.plot(x_data, y_data,label='Learner Model')
# plt.plot(x_solution, y_solution,label='Solution Model')
plt.legend()
plt.show()
