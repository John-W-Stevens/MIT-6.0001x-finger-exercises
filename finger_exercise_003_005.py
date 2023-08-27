# Figure 3.5 code

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2*guess))
print('Square root of', k, 'is about', guess)

# Add some code to the implementation of Newton-Raphson that keeps track of the number
# of iterations used to find the root. Use that code as part of a program that compares
# the efficiency of Newton-Raphson and bisection search. (You should discover that
# Newton-Raphson is more efficient.)