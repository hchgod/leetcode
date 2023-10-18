list1 = [1,2]
length = len(list1)-1
for i in range(int(length/2)+1) :
    list1[i],list1[length-i] = list1[length-i],list1[i]
print(list1)


def subarrayProductK(nums: list, k: int):
    total = 0
    j = 2
    for i in range(len(nums)):
        for p in range(1,len(nums)):
            if p > len(nums)-1:
                break
            if nums[i] * nums[p] == k:
                total = total + 1
                while nums[j] == 1:
                    total = total + 1
                    j = j + 1
    return total

if __name__ == '__main__':
    print(subarrayProductK([1, 2, 3],3))