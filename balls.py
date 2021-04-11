# balls
from itertools import chain, product
alphabet = "abcdefghijklmnopqrstuvwyz"
def x(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

print(list(filter(lambda x : x == "balls", list(x(alphabet, 5))))[0])
  
