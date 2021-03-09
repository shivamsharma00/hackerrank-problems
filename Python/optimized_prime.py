'''
This code checks wheather given number is prime or not, but this is an optimized program. Rather than,
iterating over numbers till given value we use 6k+-1 method.

This code is taken from : https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

We can do the following optimizations: 
* Instead of checking till n, we can check till √n because a larger factor of n
  must be a multiple of a smaller factor that has been already checked.

* The algorithm can be improved further by observing that all primes are of the form 6k ± 1, 
  with the exception of 2 and 3. This is because all integers can be expressed as (6k + i)
  for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4);
  and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3,
  then to check through all the numbers of form 6k ± 1.
'''

def isPrime(num):

    # Corner cases 
    if num<=1:
        return False
    if num<=3:
        return True
    
    # This is checked so that we can skip 
    # middle five numbers in below loop.
    if (num%2==0 or num%3==0):
        return False

    i = 5
    while (i*i <= num):
        if ((num%i == 0) or (num%(i+2) == 0)):
            return False
        
        i = i + 6
    return True


# Driver Program
if __name__ == '__main__':
    arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 907]
    for i in arr:
        print('Prime') if isPrime(i) else print('Not prime')
    # print('Prime') if isPrime(237) else print('Not prime')
    # print('Prime') if isPrime(431) else print('Not prime')



    
