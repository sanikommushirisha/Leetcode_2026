Backtracking algorithms use Depth-First Search to search all possible paths for a solution to a path

This brute force process of testing all possible paths and backtracking upon failure
- Explore all possible paths.
- "pruning" -> Skip entire subtrees we know can't lead to a valid solution.
- "backtracks" to the previous path as soon as the current path doesn't lead to a solution.
- Termination condition: Condition that specifies when a path should end. This condition should define when we've found a valid and/or invalid solution.

State space tree
A conceptual tree constructed by considering every possible decision that can be made at each point in a process.

- Root node: The root node represents the initial state or position before any decisions are made.
- Edges: Each edge represents a possible decision, move, or action.
- Intermediate nodes: Nodes representing partially completed states or intermediate positions.
- Leaf nodes: The leaf nodes represent complete or invalid solutions.
- Path: A path from the root to any leaf node represents a sequence of decisions that lead to a complete or invalid solution.

Drawing out the state space tree for a problem helps to visualize the entire solution space, and all possible decisions

```
def dfs(state):
    # Termination condition.
    if meets_termination_condition(state):
        process_solution(state)
        return

    # Explore each possible decision that can be made at the current state.
    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision) # Backtrack.
```

Analyzing time complexity
- Branching factor: The number of children each node has.
- Depth: The length of the deepest path in the state space tree.

The time complexity is often estimated as O(b*d)