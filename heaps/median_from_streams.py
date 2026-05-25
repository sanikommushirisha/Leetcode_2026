import heapq

def median_stream(nums, adds):
    lower = []
    upper = []

    def add_num(value):
        if upper and value > upper[0]:
            heapq.heappush(upper, value)
        else:
            heapq.heappush(lower, -value)
        
        # Rebalance heaps
        len1, len2 = len(lower), len(upper)
        if len1 > len2 + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len2 > len1:
            heapq.heappush(lower, -heapq.heappop(upper))

    def get_median():
        if len(lower) == len(upper):
            return (-lower[0] + upper[0]) / 2
        return -lower[0]

    for num in nums:
        add_num(num)

    result = []
    for val in adds:
        add_num(val)
        result.append(get_median())
    
    return result