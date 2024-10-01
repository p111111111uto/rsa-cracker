import gmpy2

e = # enter  value
p = # enter value
q = # enter value
n = p * q

c = [
 # enter values
]

phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)

for i in c:
    m = pow(i, d, n)
    print(chr(m))