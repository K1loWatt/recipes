def findSmallest(arr: list[int]) -> int:
    """
    This function finds the smallest element in an array and returns its index.
    """

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: list[int]) -> list[int]:
    """
    This function sorts an array using the selection sort algorithm.
    """

    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == "__main__":
    print(selectionSort([5, 3, 6, 2, 10]))
