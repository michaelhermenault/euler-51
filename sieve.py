
def sieve(num_list, prime_list):
  #Remove all elements divisible by the last element in the prime list
  num_list = [element for element in num_list if element % prime_list[-1] != 0]
  #Base case if all numbers have been elminated.
  if(len(num_list) == 0):
    return prime_list
  #Otherwise append lowest number left in num list to the prime list
  prime_list.append(num_list.pop(0))
  #Recurse
  return sieve(num_list, prime_list)
  
print(sieve(range(3,121), [2]))
