import numpy as np

h = [0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0]
t = [1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1]

# convert to numpy arrays
h = np.array(h)
t = np.array(t)

# count heads and tails
heads = np.count_nonzero(h == 1)
tails = np.count_nonzero(h == 0)

print("Heads:", heads)
print("Tails:", tails)