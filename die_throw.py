import numpy as np

n = 1000   # number of coin tosses

dice = np.random.randint(1, 7, n)

print("Dice throw results:", dice)

counts = np.bincount(dice)[1:]

print("1 appeared:", counts[0])
print("2 appeared:", counts[1])
print("3 appeared:", counts[2])
print("4 appeared:", counts[3])
print("5 appeared:", counts[4])
print("6 appeared:", counts[5])
print("prob is : ",counts[0]/n)
print("prob is : ",counts[1]/n)
print("prob is : ",counts[2]/n)
print("prob is : ",counts[3]/n)
print("prob is : ",counts[4]/n)
print("prob is : ",counts[5]/n)
print("total prob is: ",(counts[0]+counts[1]+counts[2]+counts[3]+counts[4]+counts[5])/n)
'''heads = np.sum(toss)
tails = n - heads

print("Heads:", heads)
print("Tails:", tails)'''
