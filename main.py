'''In a sumac sequence, t1, t2, .., tm, each term is an integer greater than or equal 0. Also, each term,
starting with the third, is the difference of the preceding two terms (that is, tn+2 = tn − tn+1 for
n ≥ 1). The sequence terminates at tm if tm−1 < tm.
For example, if we have 120 and 71, then the sumac sequence generated is as follows:
120, 71, 49, 22, 27.
This is a sumac sequence of length 5.
Input Specification
The input will be two positive numbers t1 and t2, with 0 < t2 < t1 < 10000.
'''

def sumac_sequence_length(t1, t2):
    sequence_length = 2  # Initialize the length with 2 (for t1 and t2)
    while t2 <= t1:
        t1, t2 = t2, t1 - t2
        sequence_length += 1
    return sequence_length

# Read input
t1 = int(input())
t2 = int(input())

# Calculate the length of the sumac sequence
result = sumac_sequence_length(t1, t2)

# Print the result
print(result)