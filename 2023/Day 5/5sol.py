from functools import reduce
from itertools import chain
from re import findall

(f:=open("input.txt").read().split('\n\n')) and print(min(reduce((lambda s, m: (z:=map(int, findall(r'\d+', m))) and (p:=[*zip(z, z, z)]) and [next(((u + x - v, l) for u,v,w in p if v <= x and x + l <= v + w), (x, l)) for x,l in reduce((lambda r, a:{*chain(*([(x, a - x), (a, x + l - a)] if x < a < x + l else [(x, l)] for x,l in r))}), chain(*((v, v + w) for _,v,w in p)), s)]), f[1:], (i:=map(int, findall(r'\d+', f[0]))) and [*zip(i, i)]))[0])