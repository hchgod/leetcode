# @Time : 2023/9/25 16:18
def fun(nums: list):
    result_max = 0
    df= nums[0]
    for i in range(1, len(nums)):
        df = max(df + nums[i], nums[i])
        result_max = max(df,result_max)
    return result_max


if __name__ == '__main__':
    print(fun([-1, 3, 2, -3, 1,-1,10]))
