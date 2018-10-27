import datetime
import time

def log(fn):
  def wrap(*args):
    start = datetime.datetime.now()
    res = fn(*args)
    duratime = datetime.datetime.now() - start
    # print('%s takes %ds' %(fn.__name__, duratime.total_seconds()))
    print("function {} took {}s".format(fn.__name__, duratime.total_seconds()))
    return res
  return wrap

@log
def isPrime(prime):
  if prime > 0:
    if prime == 1:
      return '1 is not prime' 
    else:  
      for num in range(2, prime):
        if(prime % num == 0):
          return print('%d is not prime, it can be exact by %d' %(prime, num))
      else:
        return print('%d is prime' %prime)  
  else:
    return print('Error, input must > 0')

prime = int(input('input num to check is prime number\n> '))

isPrime(prime)   