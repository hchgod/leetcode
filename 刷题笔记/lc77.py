def combine(self, n: int, k: int):
    result = []
    begin = 1
    self.backtracking(n, k, result, begin, [])
    return result


def backtracking(self, n, k, result, begin, ls):
    if (len(ls) == k):
        result.append(ls[:])
        return

    for i in range(begin, n + 1):
        ls.append(i)
        self.backtracking(n, k, result, i + 1, ls)
        ls.pop()


if __name__ == '__main__':
    fun(4,2)
