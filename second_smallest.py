def second_smallest(list_item):
    if len(list_item) < 2:
        return None
    smallest = float('inf')
    sec_smallest = float('inf')
    for num in list_item:
        if num < smallest:
            sec_smallest = smallest
            smallest = num
        elif num < sec_smallest:
            sec_smallest = num
    return sec_smallest

print(second_smallest([5, 8, 3, 2, 6]))