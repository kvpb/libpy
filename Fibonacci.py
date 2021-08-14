#def nF( n ):
#  return -1**( -( n ) + 1 ) * F( -( n ) )
# KVPB's RCSVNFIB

def F( n ):
  if ( n < 0 ):
    return ( -1 )**( -( n ) + 1 ) * F( -( n ) ) #return ( -1 )**abs( n + 1 ) * F( -( n ) ) # It was a precedence issue. Thanks, Linek. #return -F( -n ) #return nF( n )
  if ( n <= 1 ):
    return n
  return F( n - 1 ) + F( n - 2 )
# KVPB's RCSVFIB

#print(F( -20 ))
#print(F( -10 ))
#print(F(  -5 ))
#print(F(  -3 ))
#print(F(  -2 ))
#print(F(  -1 ))
#print(F(   0 ))
#print(F(   1 ))
#print(F(   2 ))
#print(F(   3 ))
#print(F(   5 ))
#print(F(  10 ))
#print(F(  20 ))
#i = -20
#while ( i <= 20 ):
#  print(F( i ))
#  i += 1
#   debug code

# Fibonacci.py
# Fibonacci number
#
# Karl V. P. Bertin `kvpb`
# +33 A BB BB BB BB
# local-part@domain
# https://www.linkedin.com/in/karlbertin

