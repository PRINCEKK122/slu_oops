def isPrime(number, divisor = None):
    if number <= 1:
        return False
    
    if divisor is None:
        divisor = number - 1
    
    if divisor == 1:
        return True
    elif number % divisor == 0:
        return False
    
    return isPrime(number, divisor - 1)


def primeFactors(number, divisor = 2):
    if number <= 1:
        return []
    if number % divisor == 0 and isPrime(divisor):
        return [divisor] + primeFactors(number // divisor, divisor)
    return primeFactors(number, divisor + 1)

if __name__ == "__main__":
    number = int(input("Enter a number: "))

    print(primeFactors(number))
    