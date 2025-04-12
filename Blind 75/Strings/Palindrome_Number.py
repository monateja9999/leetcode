class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        new_num = 0

        while (num // 10) != 0:
            new_num += num % 10
            new_num *= 10
            num = num // 10
        new_num+=num
        if x == new_num:
            return True
        else:
            return False