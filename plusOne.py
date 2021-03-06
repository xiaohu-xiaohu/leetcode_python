class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits

digits = [1, 9, 9]

result = Solution()

print(result.plusOne(digits))