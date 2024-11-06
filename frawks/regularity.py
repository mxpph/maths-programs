import numpy as np
import mpmath
import pickle

# finds the fractions that have each digit uniformly distributed 
# in the expansion.
# eg. 1/61 has each digit 0-9 six times.
def main():
    uniformDenoms = []
    # Dictionary to store periods of numbers 1-10000
    A007732 = pickle.load(open("A007732.p", "rb"))
    for denominator in range(2, 10000):
        period = A007732[denominator]
        if period < 10 or period % 10 != 0:
            continue

        mpmath.mp.dps = period + 1

        # If the denominator is coprime to 10, the fraction repeats.
        if np.gcd(denominator, 10) != 1:
            continue

        numerator = int(10 ** (np.floor(np.log10(denominator)) - 1))
        frac = str(mpmath.fdiv(numerator, denominator))
        frac = frac[2:-2]
        digits = {f"{i}": 0 for i in range(0, 10)}
        for d in frac:
            digits[d] += 1
        if list(digits.values()).count(digits["0"]) == len(digits.values()):
            uniformDenoms.append((numerator, denominator))

    for p in uniformDenoms:
        print(p)


if __name__ == '__main__':
    main()
