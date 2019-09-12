
def sieve(num_list, prime_list):
  num_list = [element for element in num_list if element % prime_list[-1] != 0]
  if(len(num_list) == 0):
    return prime_list
  prime_list.append(num_list.pop(0))
  return sieve(num_list, prime_list)
  
#for element in range(3,100):
#  print(element)
print(sieve(range(3,121), [2]))

def find_prime_family(ceiling):
  primes = sieve(range(3,ceiling),[2])
  for(prime in primes):
    

def all_families(num_elements):
  if num_elements == 1:
    return [[True],[False]]
  [ [True] + element
