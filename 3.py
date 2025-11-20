import numpy as np
import matplotlib.pyplot as plt
n = int(input("Enter number of computers: "))
steps = int(input("Enter number of steps: "))
infect_rate = float(input("Enter infection rate (0-1): "))
detect_rate = float(input("Enter detection rate (0-1): "))
state = np.zeros(n, int)
state[np.random.choice(n, 1)] = 1   # one infected
healthy, infected, detected = [], [], []
for _ in range(steps):
    new = state.copy()
    for i in range(n):
        if state[i] == 1:
            for c in np.random.choice(n, 3, replace=False):
                if state[c] == 0 and np.random.rand() < infect_rate:
                    new[c] = 1
            if np.random.rand() < detect_rate:
                new[i] = 2
    state = new
    healthy.append(sum(state == 0))
    infected.append(sum(state == 1))
    detected.append(sum(state == 2))
plt.plot(healthy, label='Healthy')
plt.plot(infected, label='Infected')
plt.plot(detected, label='Detected')
plt.xlabel("Steps"); plt.ylabel("Computers")
plt.title("Virus Spread Simulation")
plt.legend(); plt.show()