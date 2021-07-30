def nF( n ):
  if ( n >= 0 ):
    return F( n )
  #if ( n == -1 ):
  #  return -( n )
  else:# if ( -2 >= n ):
    return -1**( n + 1 ) * ( nF( n - 1 ) + nF( n - 2 ) ) #return -1**( n + 1 ) * F( n )
# KVPB's RCSVNFIB

def F( n ):
  if ( n < 0 ):
    return nF( n )
  if ( 0 <= n ) and ( n <= 1 ):
    return n
  else:# if ( 2 < n ):
    return F( n - 1 ) + F( n - 2 )
# KVPB's RCSVFIB

print(F( -3 ))
print(F( -2 ))
print(F( -1 ))
print(F(  0 ))
print(F(  1 ))
print(F(  2 ))
print(F(  3 ))
#   debug code

# Fibonacci.py
# Fibonacci number
#
# Karl V. P. Bertin `kvpb`
# +33 A BB BB BB BB
# local-part@domain
# https://www.linkedin.com/in/karlbertin

