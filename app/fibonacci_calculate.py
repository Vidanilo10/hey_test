from math import sqrt

def validate_pandigitall(s: str) -> bool:
    return set(s) == set("123456789")

def get_image(x: float, n: int) -> float:
    res: float = 1.0
    for i in range(n):
        res *= x
        if res > 1e20:
            res *= 1e-10
    return res

def get_nine_digits(n: int) -> bool:
    F: float = get_image((1 + sqrt(5)) / 2, n) / sqrt(5)
    s: str = "%f" % F
    if validate_pandigitall(s[:9]):
        return True


def main():
    a: int = 1
    b: int = 1
    n: int = 1

    while True:
        if validate_pandigitall(str(a)[-9:]):
            if get_nine_digits(n):
                break
        a, b = b, a + b
        b = b % 1000000000
        n += 1
    return n


if __name__ == "__main__":
    main()

