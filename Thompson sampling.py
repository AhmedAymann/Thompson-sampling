# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing the Dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")


# implementing Thompson sampling
import random

round_number = 10000
Ad_number = 10
adds_selected = []



numbers_of_rewards_1 = [0] * Ad_number
numbers_of_rewards_0 = [0] * Ad_number
total_reward = 0
for n in  range(0, round_number):
    ad = 0
    max_random = 0
    for i in range(0, Ad_number):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    adds_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward
    
    
# visualising the results
plt.hist(adds_selected)
plt.title("histogram of ads selections")
plt.xlabel("ads")
plt.ylabel("number of selections")
plt.show()