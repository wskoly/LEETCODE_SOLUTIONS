class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        num_str = f"-{str(x)[1:][::-1]}" if is_negative else str(x)[::-1]
        print(num_str)
        x = int(num_str)
        return x if (-2**31)<=x<=((2**31)-1) else 0