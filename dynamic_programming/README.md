Some problems can be broken down into subproblems and these sub problems are smaller versions of main problems.
We can solve thus Using recursion/backtracking, but you risk resolving the same sub problems various time
For increased performance, Store solutions to sub problems so that you can solve them atmost once.

# How to identify DP Problems:

- Optimal substructure
- Overlapping sub problems
- Recurrence relation: A formula that expresses the solution to the problem in terms of the solutions to its subproblems.
- Base cases

# How to approach:

- Find the Recurrence Relation
- Identify the Base Case(s)
- Write the Recursive Solution
- Add Memoization
- Convert to "Bottom-Up" DP
- Further Optimization

# Interview Tip

If you're having trouble coming up with the bottom-up solution, try starting with the top-down solution.
Top down: Step 1: Identify recurrence + Step 2: Apply memoization
Bottom Up: Both recurrence + memoization together

When a problem asks for the minimum or maximum of something, it might be a DP problem.

