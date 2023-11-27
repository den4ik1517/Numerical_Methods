import math

def right_rectangles(f, a, b, n):
    """
    Обчислює визначений інтеграл методом правих прямокутників

    Args:
        f: Підінтегральна функція
        a: Початкова точка інтегрування
        b: Кінцева точка інтегрування
        n: Кількість розбиттів проміжку інтегрування

    Returns:
        Значення інтеграла
    """

    h = (b - a) / n
    x = [a + i * h for i in range(n)]
    y = [f(xi) for xi in x]

    return h * sum(y)


def main():
    f = lambda x: x * math.exp(3 * x)
    a = 1
    b = 2
    n = 30

    print(right_rectangles(f, a, b, n))


if __name__ == "__main__":
    main()
