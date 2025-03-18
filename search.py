import os

num_simulations = 5

for i in range(num_simulations):
    os.system("python generate.py")

    os.system("python simulate.py")