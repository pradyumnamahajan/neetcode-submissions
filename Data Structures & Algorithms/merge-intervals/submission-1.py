class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        start, end = intervals[0]

        answer = []
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            
            i_start, i_end = interval

            if i_start > end:
                answer.append([start, end])
                start = i_start
                end = i_end
            elif i_end > end:
                end = i_end

        answer.append([start, end])

        return answer