def fun(nums:list):
    result = []
    ls = []
    vistied = {}
    for i in nums:
        vistied[i] = False
    backtracking(nums, ls, vistied, result)
    return result

def backtracking(nums:list, ls:list, vistied, result):
    if len(ls) == len(nums):
        result.append(ls[:])
        return result

    for num in nums:
        if not vistied[num]:
            ls.append(num)
            vistied[num] = True
            backtracking(nums, ls, vistied, result)
            ls.pop()
            vistied[num] = False


if __name__ == '__main__':
    print(fun([1,2,3,4,5]))