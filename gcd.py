def gcd( a, b ):
  while b != 0:
    c = b
    b = a % b
    a = c
  return a # division-based Euclid's algorithm
# KVPB's GCD

#print(gcd(  4,  6 ))
#print(gcd(  6,  9 ))
#print(gcd( 20, 30 ))
#print(gcd( 42, 69 ))
#print(gcd(  0,  0 ))
#	debug code

# gcd.py
# greatest common divisor of two integers
#
# Karl V. P. B. `kvpb`    Karl T. G. West `ktgw`
# +33 A BB BB BB BB       +1 (DDD) DDD-DDDD
# local-part@domain       local-part@domain

