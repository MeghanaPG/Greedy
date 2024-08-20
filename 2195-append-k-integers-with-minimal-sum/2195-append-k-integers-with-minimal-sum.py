class Solution:
    def minimalKSum(self, A: List[int], k: int) -> int:
        A = sorted(list(set(A)))
        n = len(A)

        if A[n-1] <= k + n:
            return (k+n) * (k+n+1) // 2 - sum(A)

        
        l, r = 0, n-1
        while r > l:
            mid = (l+r) // 2
            if A[mid] - mid <= k:
                l = mid + 1
            else:
                r = mid
        
        return (k+l) * (k+l+1) // 2 - sum(A[:l])