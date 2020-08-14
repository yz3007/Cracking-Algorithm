# birthday

def birthday_1(n):
    if n <= 0: return 0

    # n is people
    base = 1

    # n!
    for i in range(1, n + 1):
        base *= i

    res = 0

    def backtrack(num, options):
        nonlocal res
        if num == n:
            res += 1
            return

        for idx, opt in enumerate(options):
            if opt == num:
                continue

            options.pop(idx)
            backtrack(num + 1, options)
            options.insert(idx, opt)

    backtrack(0, list(range(n)))

    return 1 - res / base


def birthday_2(n):
    # time O(n), space O(n)
    array = [1] * (n + 1)
    for i in range(n):
        array[i + 1] = array[i] * (i + 1)

    def comb(n, m):
        return array[n] / (array[m] * array[n - m])

    total = 0
    multiple = 1

    for i in range(1, n + 1):
        total = total + comb(n, i) * array[n - i] * multiple
        multiple *= -1

    return total / array[n]


if __name__ == '__main__':
    # print(birthday_1(20))
    print(birthday_2(100))
