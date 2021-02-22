"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

pn = [1,2]
counter = 2

while len(pn) < 20 :
    for x in pn:
        counter += 1
        if counter % x == 0 :
            break
        pn.append(counter)





print(pn)


