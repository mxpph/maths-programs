
import logging

logging.basicConfig(filename="regularity_numerators.txt", level=logging.DEBUG)
number = 100000

while number < 999999:
    a = str(number)
    n = len(a)
    i = 0
    while i <= (n - 1)//2:
        if  (abs(int(a[i]) - int(a[i+1])) !=
            abs(int(a[n//2 + i]) - int(a[(n//2 + i + 1) % n]))):
            # Not regular
            break
        else:
            i += 1
    # if no break
    else:
        logging.debug(str(number))

    number += 1
