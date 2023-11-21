from itertools import permutations,product,accumulate,combinations,groupby

pattern = ["a","v","d","d","i"]

for new in permutations(pattern):
    print("".join(new),new)
##
a = accumulate(pattern)
print(list(a))