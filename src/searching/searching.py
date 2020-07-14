# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case, if end and start are equal (0..1..etc) we stop recursing
    if end >= start:
        # we get our midpoint or 'guess'
        mid = start + end // 2
        #if our guess is what we are looking for
        if arr[mid] == target:
            # return index of its location
            return mid

        #if our guess is not what we are looking for
        #if our guess is too high
        elif arr[mid] > target:
            #recurse
            # we eliminate the top half of our search by setting mid - 1 as our new end
            return binary_search(arr, target, start, mid - 1)

        #if our guess is too low
        else:
            #recurse
            # we eliminate the bottom half of our search by setting mid + 1 as our new start
            return binary_search(arr, target, mid + 1, end)

    else:
        # if we don't find a match, we return negative 1 per the test env
        return -1


    

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

