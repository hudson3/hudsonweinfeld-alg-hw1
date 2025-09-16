"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    # x is how many in the sequence
    # sequence is the list containing the sequence

    sequence = [0, 1]

    num1 = 0
    num2 = 1

    for a in x:
        # find number to append
        num3 = num1 + num2

        # set new last two numbers
        num1 = num2
        num2 = num3

        sequence.append(num3)

        return sequence

    

def longest_run(mylist, key):

    current_streak = 0
    best_streak = 0

    for current_num in mylist:
        if current_num == key:
            current_streak += current_streak

        if current_streak > best_streak:
            best_streak = current_streak
    
    return best_streak


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
    pass



