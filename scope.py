def factorial(n: int) -> int:
    """
    Calculates the factorial of n recursively
    :param n: the number
    :return: the result
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n: int) -> int:
    """
    Calculates the factorial of n iteratively
    :param n: the number
    :return: the result
    """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def fibonacci(n: int) -> int:
    """Return the `nth` Fibonacci number, or positive `n`.
    A fibonacci number is a number made by adding the previous two values.
    This means the first thirteen Fibonacci numbers, starting from 0 are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. This has been executed iteratively."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


def fibonacci2(n: int) -> int:
    """Return the `nth` Fibonacci number, or positive `n`.
     A fibonacci number is a number made by adding the previous two values.
    This means the first thirteen Fibonacci numbers, starting from 0 are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. This has been executed recursively."""
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(36):
    print(i, ": ", fibonacci2(i))