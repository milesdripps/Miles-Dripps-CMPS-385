def insertion_sort(arr):
    """
    Starting at number at index 1, we compare every number up to that index
    If number is less than another number, we swap number down to that number
    O(n^2) worst time complexity, since we are comparing every element to itself
    """
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]: # if number is less than the first number before it
                h, k = i, i
                while h != k: # Swap down to the same index
                    arr[h], arr[h-1] = arr[h-1], arr[h]
                    h -= 1
                break
    return arr

def main():
    #Example lists
    lists = [[5,1,2,9,12,3,6],
             [200,197,190,23,200,1],
             [9,100,22,3,44,0]
             ]

    for arr in lists:
        print(f"{arr} --(Insertion Sort)--> {insertion_sort(arr)}")

main()
