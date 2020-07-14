# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Your code here
    # pointer for left index
    l_indx = 0
    # pointer for right index
    r_indx = 0
    # our final merged arr in list
    merged_arr = []
    # while our left index is less than length of both left and right
    # (arrA, arrB)
    while l_indx < len(arrA) and r_indx < len(arrB):
        # if the index value at left is less than right
        if arrA[l_indx] < arrB[r_indx]:
            #append the index of left (arrA) to our merged_arr
            merged_arr.append(arrA[l_indx])
            # increment the index to handle more than 1 index
            l_indx += 1
        else:
            #append the index of right (arrB) to our merged_arr
            merged_arr.append(arrB[r_indx])
            # increment the index to handle more than 1 index
            r_indx += 1
    # add all the indices from the left to merged_arr
    merged_arr += arrA[l_indx:]
    # add all the indices from the right to merged_arr
    merged_arr += arrB[r_indx:]
    #return 
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here 
    # set base case
    if len(arr) <= 1:
        return arr
    #divide in half, pivot is mid
    mid = len(arr) // 2
    #recurse on the left of mid
    left = merge_sort(arr[:mid])
    #recurse on the right of mid
    right = merge_sort(arr[mid:])
    # return helper on our left and right 
    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))