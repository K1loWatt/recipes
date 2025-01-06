

def binary_search(list: list[int],item:int)->int:
    """
    This function performs a binary search on a sorted input array.
    """
    
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__=="__main__":
    my_list = [1,3,5,7,9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))