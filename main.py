"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1: # handles base cases of x = 0 or 1
        return x
    minus_one = foo(x - 1)  # recursively calls x-1
    minus_two = foo(x - 2)  # recursively calls x-2
    return minus_one + minus_two   # returns summation of 2 previous terms to find correct fibonacci number

def longest_run(mylist, key):
    ### TODO
    best = 0  # initializes variable to hold best run so far
    cur = 0   # initializes variable to hold current run
    for v in mylist:  # iterates through list
        if v == key:  # if reaches an element that matches the inputted key
            cur += 1  # extends the current run by 1
            if cur > best:  # if the current run is larger than previous best run, updates best run to current
                best = cur 
        else:  # if not, reset current run to 0 and move to next
            cur = 0
    return best


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    n = len(mylist)   # initializes variable to hold the lenght of the list
    
    if n == 0:  # handles base case that the list is empty
        return Result(0, 0, 0, True)
        
    if n == 1:  # handles base case that the lsit has only one element
        if mylist[0] == key:
            # if the single element does match the key, there is a run length of 1
            return Result(1, 1, 1, True)
        else:
            # if the single element does not match the key, there is no run length
            return Result(0, 0, 0, False)

    # handles recursive cases by spliting the list into two halves
    mid = n // 2
    left  = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)

    # checks if both halves are uniform
    is_entire = left.is_entire_range and right.is_entire_range

    # checks left and right runs by adding size, possibly extended if uniform
    left_size  = left.left_size  + (right.left_size  if left.is_entire_range  else 0)
    right_size = right.right_size + (left.right_size if right.is_entire_range else 0)

    # combines runs of left half of right and right half of left
    cross = left.right_size + right.left_size

    # finds the maximum runtime of left, right, and cross
    longest = max(left.longest_size, right.longest_size, cross)

    # returns a combined result
    return Result(left_size, right_size, longest, is_entire)



