def merge_sort (lst):
    """
    Sorts a list into ascending order.
    returns a new sorted list.
    1 - divide - find the mindpoint of the list and divite into sublists.
    2 - conquer - recursively sort the sublists from the previous step.
    3 - combine - merge the sublists from the previous steps.
    """
    if len(lst) <= 1 :
        return lst

    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(lst):
    """
    Divides the unsorted list into sublists at midpoint.
    Returns two sublists, left and right.
    """
    mid = len(lst)/2
    left = lst[:mid]
    right = lst[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (left and right), sorting them in the process.
    Returns a new sorted list.
    """

    l = []
    i = 0 
    j = 0 

    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

