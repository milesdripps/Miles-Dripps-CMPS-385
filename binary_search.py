import math

def binary_search(arr, start, end, target):
    print(f"[{arr[start]}] - [{arr[end]}]")
    """

    :param arr:         array of numbers
    :param end:         end index of array, initialized as last digit in array
    :param target:      number to be found
    :return:
    """
    middle = math.floor((start+end)/2)
    print(f"[{arr[start]}] - [{arr[middle]}] - [{arr[end]}]")

    if arr[middle] == target:
        print(f"found {target} at index {middle}")
    elif start == end:
        print(f"{target} not in list")
    elif target < arr[middle]:
        binary_search(arr, 0, middle - 1, target)
    elif target > arr[middle]:
        binary_search(arr, middle + 1, end, target)

    return middle

def main():
    arrays = {
        7 : [1,2,3,4,5,6,7,8],
        80: [10, 20, 30, 40, 50, 60, 70, 80] ,
        10 : [10, 20, 30, 40, 50, 60, 70, 80] ,
        40 : [10, 20, 30, 40, 50, 60, 70, 80] ,
        31 : [10, 20, 30, 40, 50, 60, 70, 80],
        11: [10, 20, 30, 40, 50, 60, 70, 80]

    }

    for target, arr in arrays.items():
        print(f"{arr} with target {target}:")
        binary_search(arr,0,len(arr)-1,target)



main()