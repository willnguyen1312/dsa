def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


print(binary_search([1,2,3,4,5], 3, 0, 4))
print(binary_search([1,2,3,4,5], 13, 0, 4))