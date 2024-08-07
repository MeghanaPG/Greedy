class Solution:
    import math
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        res = 0
        num_days = 0
        jobs.sort()
        workers.sort()

        for i in range(len(jobs)):
            num_days = math.ceil(jobs[i]/workers[i])
            res = max(num_days, res)
        return res 
        