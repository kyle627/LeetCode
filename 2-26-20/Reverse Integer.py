class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            answer = int(str(x)[::-1])
        if x <= 0:
            answer = -1 * int(str(x * -1)[::-1])

        min = -2 ** 31
        max = 2 ** 31 - 1

        if answer not in range(min, max):
            return 0
        else:
            return answer
