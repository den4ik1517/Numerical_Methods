import math


def simpson(f, a, b, m):
    """
    Обчислює визначений інтеграл методом Симпсона

    Args:
        f: Підінтегральна функція
        a: Початкова точка інтегрування
        b: Кінцева точка інтегрування
        m: Кількість розбиттів проміжку інтегрування

    Returns:
        Значення інтеграла
    """

    h = (b - a) / m
    x = [a + i * h for i in range(m + 1)]
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]  # додаємо значення на початку і в кінці

    # додаємо подвійні значення
    for i in range(1, m, 2):
        result += 4 * y[i]

    # додаємо потрійні значення
    for i in range(2, m - 1, 2):
        result += 2 * y[i]

    return (h / 3) * result


def main():
    f = lambda x: x * math.exp(3 * x)
    a = 1
    b = 2
    m = 10

    print(simpson(f, a, b, m))


if __name__ == "__main__":
    main()
