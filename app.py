
def is_prime(number: int) -> bool:
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def next_three_primes(start: int) -> list[int]:
    """Return the first three prime numbers greater than start."""
    primes = []
    candidate = start + 1

    while len(primes) < 3:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes


def main() -> None:
    user_input = input("Inserisci un numero intero: ")
    number = int(user_input)

    primes = next_three_primes(number)
    print(f"I primi 3 numeri primi successivi a {number} sono: {primes[0]}, {primes[1]}, {primes[2]}")


if __name__ == "__main__":
    main()
