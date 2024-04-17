import numpy as np
import matplotlib.pyplot as plt

# Parameters
population = np.zeros((100,100))
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery rate

# Initialize random outbreak
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Function to infect neighbors
def infect_neighbors(x, y):
    for i in range( x- 1, x + 2):
        for j in range (y - 1, y + 2):
            if i!=x or j!=y:
                if 0<=i<100 and 0<=j<100: #within the bond
                    if (i, j) != (x, y) and population[i, j] == 0: # to ensure it do not infect itself but infect the ones that are already "susceptible"
                        population[i, j] = np.random.choice(range(2), 1, p=[1 - beta, beta])[0]

                    

# Function to recover individuals
def recover_individuals():
    for x in range(100):
        for y in range(100):
            if population[x, y] == 1: #the infected people
                if np.random.random() < gamma:#in order word, this code simulate the probability of having recovery by comparing the the randomly generate a number between 0 and 1 to the standard recovery rate
                    population[x, y] = 2  #recovered

# Simulate infection spread over 100 times
for time in range(100):
    for x in range(100):
        for y in range(100):
            if population[x, y] == 1:
                infect_neighbors(x, y)
    recover_individuals()

    # Plot heatmap for each time point
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f"Time Point: {time}")
    plt.show()
