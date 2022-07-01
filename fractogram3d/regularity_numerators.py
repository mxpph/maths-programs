
import logging

logging.basicConfig(filename="regularity_numerators.txt", level=logging.DEBUG)
number = 100000
nums = []

while number < 999999:
    a = [int(x) for x in list(str(number))] #
    n = len(a)
    i = 0
    while i <= (n - 1)//2:
        if abs(a[i] - a[i+1]) != abs(a[n//2 + i] - a[(n//2 + i + 1) % n]):
            break
        else:
            i += 1
    # if no break
    else:
        logging.debug(str(number))

    number += 1
