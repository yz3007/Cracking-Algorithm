# birthday

在一次生日派对中，有 n 个孩子参加了派对，他们决定相互赠送礼物。他们赠送礼物的方式是：首先将每

个人的名字写在一张纸条上，然后放入一个不透明的盒子内，接下来每个孩子都会从盒子中随机拿走一张

纸条，这样最后每个孩子都会拿到一张纸条。然后每一个孩子会给自己拿到的纸条上对应的那个人送礼物。

但是这个方式有一个问题，就是有些孩子可能会拿到写着自己名字的纸条，那么他们就会不开心。现在你

需要计算一下会出现这种情况的概率是多少，即至少有一个孩子拿到写着自己名字的纸条的概率。

输入描述：

第一行包含一个整数?，表示孩子的个数。1 ≤ ? ≤ 1012

输出描述：

输出对应的答案，保留四位小数。

输入样例 1

2

输出样例 1：

0.50

输入样例 2：

3

输出样例 2：

0.66

# backtracking
def birthday_1(n):
    if n <= 0: return 0

    # n is people
    base = 1

    # n!
    for i in range(1, n + 1):
        base *= i

    res = 0

    def backtrack(num, options):
        # time O(N!), space O(N)
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

#容斥原理
#https://baike.baidu.com/item/%E5%AE%B9%E6%96%A5%E5%8E%9F%E7%90%86/10146840?fr=aladdin
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
