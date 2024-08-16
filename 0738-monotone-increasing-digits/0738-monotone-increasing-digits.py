class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # to find the largest number <= N which has monotonic increasing sequence
        if n < 10:
            return n 

        num, inv_idx = n, -1
        rev_num_array = [int(digit) for digit in str(n)][::-1]

        # find the leftmost position that is inverted 
        for i in range(1, len(rev_num_array)):
            if rev_num_array[i] > rev_num_array[i-1] or (inv_idx != -1 and rev_num_array[inv_idx] == rev_num_array[i]):
                # storing the inverted pos index
                inv_idx = i 

        if inv_idx == -1:
            return n

        for i in range(inv_idx): 
            rev_num_array[i] = 9
        rev_num_array[inv_idx] -= 1 
                
        return int(''.join([str(i) for i in rev_num_array[::-1]]))
       
