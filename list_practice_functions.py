"""
List Practice Functions - Progressive Difficulty
For students learning functions and lists
"""

# ===== WARM-UP EXERCISES =====

def sum_of_list(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Example:
        sum_of_list([1, 2, 3, 4]) returns 10
        sum_of_list([10, -5, 3]) returns 8
    """
    total = 0
    for num in numbers:
        total += num
    return total


def count_evens(numbers):
    """
    Count how many even numbers are in the list.
    
    Example:
        count_evens([1, 2, 3, 4, 5, 6]) returns 3
        count_evens([1, 3, 5]) returns 0
    """
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


def find_maximum(numbers):
    """
    Find the largest number in the list.
    Assume the list is not empty.
    
    Example:
        find_maximum([3, 7, 2, 9, 1]) returns 9
        find_maximum([-5, -2, -10]) returns -2
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# ===== INTERMEDIATE CHALLENGES =====

def reverse_list(items):
    """
    Return a new list with all elements in reverse order.
    Do NOT use the built-in reverse() method or [::-1] slicing.
    
    Example:
        reverse_list([1, 2, 3, 4]) returns [4, 3, 2, 1]
        reverse_list(['a', 'b', 'c']) returns ['c', 'b', 'a']
    """
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items


def filter_positives(numbers):
    """
    Create a new list containing only the positive numbers.
    Zero is not considered positive.
    
    Example:
        filter_positives([1, -2, 3, -4, 5]) returns [1, 3, 5]
        filter_positives([-1, -2, -3]) returns []
    """
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives


def find_all_indices(items, target):
    """
    Find all positions (indices) where target appears in the list.
    Return a list of indices.
    
    Example:
        find_all_indices([1, 2, 3, 2, 4, 2], 2) returns [1, 3, 5]
        find_all_indices(['a', 'b', 'c'], 'd') returns []
    """
    indices = []
    for i in range(len(items)):
        if items[i] == target:
            indices.append(i)
    return indices


# ===== ADVANCED PROBLEMS =====

def remove_duplicates(items):
    """
    Return a new list with duplicates removed, keeping first occurrence.
    Maintain the original order.
    
    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4]) returns [1, 2, 3, 4]
        remove_duplicates(['a', 'b', 'a', 'c']) returns ['a', 'b', 'c']
    """
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def chunk_list(items, chunk_size):
    """
    Split a list into smaller lists (chunks) of given size.
    The last chunk may be smaller if items don't divide evenly.
    
    Example:
        chunk_list([1, 2, 3, 4, 5, 6, 7], 3) returns [[1, 2, 3], [4, 5, 6], [7]]
        chunk_list(['a', 'b', 'c', 'd'], 2) returns [['a', 'b'], ['c', 'd']]
    """
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunk = []
        for j in range(i, min(i + chunk_size, len(items))):
            chunk.append(items[j])
        chunks.append(chunk)
    return chunks


# ===== TEST YOUR FUNCTIONS =====

if __name__ == "__main__":
    print("Testing list functions...\n")
    
    # Test sum_of_list
    print("sum_of_list([1, 2, 3, 4]):", sum_of_list([1, 2, 3, 4]))
    
    # Test count_evens
    print("count_evens([1, 2, 3, 4, 5, 6]):", count_evens([1, 2, 3, 4, 5, 6]))
    
    # Test find_maximum
    print("find_maximum([3, 7, 2, 9, 1]):", find_maximum([3, 7, 2, 9, 1]))
    
    # Test reverse_list
    print("reverse_list([1, 2, 3, 4]):", reverse_list([1, 2, 3, 4]))
    
    # Test filter_positives
    print("filter_positives([1, -2, 3, -4, 5]):", filter_positives([1, -2, 3, -4, 5]))
    
    # Test find_all_indices
    print("find_all_indices([1, 2, 3, 2, 4, 2], 2):", find_all_indices([1, 2, 3, 2, 4, 2], 2))
    
    # Test remove_duplicates
    print("remove_duplicates([1, 2, 2, 3, 1, 4]):", remove_duplicates([1, 2, 2, 3, 1, 4]))
    
    # Test chunk_list
    print("chunk_list([1, 2, 3, 4, 5, 6, 7], 3):", chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
