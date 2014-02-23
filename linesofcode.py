"""count the lines of code in eppy"""
import os
from itertools import chain, tee

aa = ((a, b, c) for a, b, c in os.walk('./'))
k = ((a,  [j for j in c if j.endswith('.py') and not j.startswith('iddv')]) for a, b, c in aa)
k1, k2, k3 = tee(k, 3)

fpaths1 = ([os.path.join(d, f) for f in fs] for d, fs in k1) #all code
fpaths2 = ([os.path.join(d, f) for f in fs] for d, fs in k2 if d.find('tests') != -1) # test code
fpaths3 = ([os.path.join(d, f) for f in fs] for d, fs in k3 if d.find('tests') == -1) # not test code
ch = chain.from_iterable(fpaths3)
fhandles = ((f, open(f, 'r')) for f in ch)
lines = ((sum(1 for line in fhandle), fname) for fname, fhandle in fhandles)

s = 0
for i, n in sorted(lines):
    print i, n
    s += i
print s