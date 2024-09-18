

def is_prime(n):
    if n < 2:
        return False

    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    return count == 2

def print_primes(n):
    for i in range(n):
        if is_prime(i) == True:
            print(i)


def get_primes(n):
    list_primes = []
    for i in range(n):
        if is_prime(i) == True:
            list_primes.append(i)
    
    return list_primes



def main(n):
    

    print(is_prime(n))
    print_primes(n)
    print(get_primes(n))

if __name__ == '__main__':
    main()   

                
        




    
        