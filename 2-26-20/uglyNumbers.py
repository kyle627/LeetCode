class Solution:
    def isUgly(self, num: int) -> bool:
        num = self.check(num, 2)
        num = self.check(num, 3)
        num = self.check(num, 5)
        return True if num == 1 else False

    def check(self, num, i):
        while num % i == 0 and num != 0:
            num = num / i
        return num