# Figure 15.8 code

vals = []
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random,choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.xlabel('Number of Occurances')

# In Figure 15.18, why are the bins near the middle of the histogram taller
# than the bins near the sides? Hint: think about why 7 is the most common
# outcome of rolling a pair of dice. (See textbook for diagram)