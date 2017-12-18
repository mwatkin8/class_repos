"""
A module for some useful math functions

Copyright Michael Watkins
"""
import numpy as np

def gcd(a,b):
    """
    The function takes as positional arguments two positive integers and returns the greatest common divisor of those two numbers and the number of iterations required to find the answer.
    
    Arguments:
        a: An integer greater than zero.
        b: An integer greater than zero.
        
    Returns:
        -1: If a or b are not integers.
        -2: If a or b are integers but are not greater than 0.
        If a and b are both positive integers then return value will be the greatest common divisor.
    """
    try:
        if isinstance(a,int) and isinstance(b,int):
            if a >= 0 and b >= 0:
                a_val = a
                if a < b:
                    a = b
                    b = a_val
                while True:
                    r = a%b
                    if r == 0:
                        return b
                    a=b
                    b=r
            else:
                return -2
        else:
            return -1
                
    except TypeError:
        return -1

def sieve_primes(N=100):
    """
    This function finds all the prime numbers between 2 and some number N.
    
    N: the high bound of our target prime number array.
    returns: A tuple of all the prime numbers between 2 and N in numeric order.
    """
    all_nums = np.arange(2,N+1)
    primes = []
    for i in range(len(all_nums)):
        if all_nums[i] != -1:           
            primes.append(all_nums[i])
            all_nums[i+all_nums[i]::all_nums[i]] = -1
       
    return tuple(primes)
