def first_occurrence(arr):
    if not arr:
        return None
    first_element = arr[0]
    if isinstance(first_element, int):
        return first_element
    if isinstance(first_element, list):
        result = first_occurrence(first_element)
        if result is not None:
            return result
    
    return first_occurrence(arr[1:])


arr = ['a', 'b', [[[[['a', 'b']]]]], [], [1]]
print(first_occurrence(arr))