class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        non_overlapping_intervals = 1
        
        start, end = intervals[0]
        for i, interval in enumerate(intervals):
            if i == 0:
                continue

            l_start, l_end = interval
            if l_start >= end:
                non_overlapping_intervals += 1
            elif l_start >= start and l_end >= end:
                continue

            start = l_start
            end = l_end
        
        return len(intervals) - non_overlapping_intervals


        # [] [] [] []
        # [   ] [   ]
        # [      ] []
