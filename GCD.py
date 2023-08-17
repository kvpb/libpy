def gcd( a, b ):
  while b != 0:
    c = b
    b = a % b
    a = c
  return a # division-based Euclid's algorithm
# KVPB's GCD

#print(nbang(  0 ))
#print(nbang(  1 ))
#print(nbang(  2 ))
#print(nbang(  3 ))
#print(nbang( 20 ))
#	debug code

# GCD.py
# greatest common divisor
#
# Karl V. P. Bertin `kvpb`  Karl T. G. West `ktgw`
# +33 A BB BB BB BB         +1 (DDD) DDD-DDDD
# local-part@domain         local-part@domain