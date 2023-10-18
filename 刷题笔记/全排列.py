class Solution:
    def permute(self, nums: list):
        result = []
        visited = {}
        for num in nums:
            visited[num] = False
        self.backtracking(nums, result, visited, [])
        return result

    def backtracking(self, nums, result, visited, ls):
        if len(ls) == len(nums):
            result.append(ls[:])
            return

        for num in nums:
            if not visited[num]:
                ls.append(num)
                visited[num] = True
                self.backtracking(nums, result, visited, ls)
                ls.pop()
                visited[num] = False
