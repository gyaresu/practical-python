# bounce.py
#
# Exercise 1.5

h = 100
for i in range(10):
    h = h * 0.6
    print(i+1, round(h, ndigits=4))
