'''
For each digit in the number, loop through the digits before it till we find a digit less than it.
If we find one such digit, we can return the next largest permutation by swapping the two, and sorting
the digits from the ones digit upto, but not including the leftmost digit swapped, in ascending order, left to right.
Otherwise, return that it is not possible.
'''

def nextLargestPermutation(x: int):

# Verify that the input is an integer
# Convert the input into a list of integers (convenient to leave each element as a string)
    assert type(x) is int, "Please enter an integer"
    x = list(str(x))

# Reverse the list so we can traverse from the beginning instead of from the end, and make a copy of it
    x.reverse()
    reverseX = list(x)

# Since we reversed the list, we just check the elements after each element
# Split the list into the element we are checking, the elements before it, and elements after it

    for i in range(len(reverseX)):
        initial = reverseX[:i] if i > 0 else []
        checking = reverseX[i]
        remaining = reverseX[i+1::]

# If we find a digit where one of digits following it is less than it, swap the two
# Reverse the list back
# Then sort the digits, left to right, in ascending order, from one digit to the right of the leftmost digit swapped, until the end
        for j in range(len(remaining)):
            if int(remaining[j]) < int(checking):
                checking, remaining[j] = remaining[j], checking
                final = initial + list(checking) + remaining
                final.reverse()
                final[-(i+j+1):] = sorted(final[-(i+j+1):])
                final = "".join(final)
                return int(final)

    print("There is no permuation that is larger")
        
    
