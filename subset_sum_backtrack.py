def subset_sum(nums, target):
    """
    Find a subset of nums that sums to target using backtracking.
    
    Args:
        nums: List of integers
        target: Target sum to achieve
    
    Returns:
        List containing the subset that sums to target, or None if no solution exists
    """
    def backtrack(idx, current_sum, path):
        # Base case: found a valid subset
        if current_sum == target:
            return path[:]
        
        # Base case: exceeded target or ran out of numbers
        if current_sum > target or idx >= len(nums):
            return None
        
        # Try including the current number
        path.append(nums[idx])
        result = backtrack(idx + 1, current_sum + nums[idx], path)
        if result is not None:
            return result
        
        # Backtrack: remove the number and try without it
        path.pop()
        result = backtrack(idx + 1, current_sum, path)
        if result is not None:
            return result
        
        return None
    
    return backtrack(0, 0, [])


def subset_sum_all(nums, target):
    """
    Find ALL subsets of nums that sum to target.
    
    Args:
        nums: List of integers
        target: Target sum to achieve
    
    Returns:
        List of lists, where each inner list is a subset that sums to target
    """
    def backtrack(idx, current_sum, path, solutions):
        # Found a valid subset
        if current_sum == target:
            solutions.append(path[:])
            return
        
        # Exceeded target or ran out of numbers
        if current_sum > target or idx >= len(nums):
            return
        
        # Try including the current number
        path.append(nums[idx])
        backtrack(idx + 1, current_sum + nums[idx], path, solutions)
        
        # Backtrack and try without it
        path.pop()
        backtrack(idx + 1, current_sum, path, solutions)
    
    solutions = []
    backtrack(0, 0, [], solutions)
    return solutions


# Example usage
if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    
    print(f"Numbers: {nums}")
    print(f"Target: {target}\n")
    
    # Find one solution
    solution = subset_sum(nums, target)
    if solution:
        print(f"One solution: {solution} (sum = {sum(solution)})")
    else:
        print("No solution found")
    
    # Find all solutions
    all_solutions = subset_sum_all(nums, target)
    print(f"\nAll solutions ({len(all_solutions)} found):")
    for sol in all_solutions:
        print(f"  {sol} (sum = {sum(sol)})")