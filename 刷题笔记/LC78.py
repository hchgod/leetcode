# @Time : 2023/9/26 10:36
import copy
def fun(nums: list):
    result = [[], ]
    ls = []
    backtraceing(nums, result, ls, 1)
    return result


def backtraceing(nums: list, result, ls, begin):
    if begin == len(nums)+1:
        return
    for i in range(begin, len(nums)+1):
        ls.append(i)
        result.append(copy.deepcopy(ls))
        backtraceing(nums, result, ls, i + 1)
        ls.pop()


if __name__ == '__main__':
    nums = [1, 2, 3,4]
    print(fun(nums))
