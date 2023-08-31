#def nfib( n ):
#  return -1**( -( n ) + 1 ) * fibonacci( -( n ) )
# KVPB's RCSVNFIB

def fibonacci( n ):
  if ( n < 0 ):
    return ( -1 )**( -( n ) + 1 ) * fibonacci( -( n ) ) #return ( -1 )**abs( n + 1 ) * fibonacci( -( n ) ) # It was a precedence issue. Thanks, Linek. #return -fibonacci( -n ) #return nfib( n )
  if ( n <= 1 ):
    return n
  return fibonacci( n - 1 ) + fibonacci( n - 2 )
# KVPB's RCSVFIB

#print(fibonacci( -20 ))
#print(fibonacci( -10 ))
#print(fibonacci(  -5 ))
#print(fibonacci(  -3 ))
#print(fibonacci(  -2 ))
#print(fibonacci(  -1 ))
#print(fibonacci(   0 ))
#print(fibonacci(   1 ))
#print(fibonacci(   2 ))
#print(fibonacci(   3 ))
#print(fibonacci(   5 ))
#print(fibonacci(  10 ))
#print(fibonacci(  20 ))
#i = -20
#while ( i <= 20 ):
#  print(fibonacci( i ))
#  i += 1
#   debug code

# fibonacci.py
# Fibonacci number
#
# Karl V. P. B. `kvpb`
# +33 A BB BB BB BB
# local-part@domain
# https://www.linkedin.com/in/

