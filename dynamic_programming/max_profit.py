#starts = [1, 3, 6, 10]
#ends = [4, 5, 10, 12]

# arr = [([1, 4], 20), ([2, 3], 20), ([6, 10], 120), ([10, 12], 70)]

# bisect.bisect: Used to locate the rightmost insertion point for an element in a sorted list to maintain its sorted order
def job_scheduling(starts, ends, profits):
    jobs = sorted(zip(starts, ends, profits), key=lambda x: x[1])
    return jobs



starts = [1, 2, 6, 10]
ends = [4, 3, 10, 12]
profits = [20, 20, 100, 70]
print(job_scheduling(starts, ends, profits))