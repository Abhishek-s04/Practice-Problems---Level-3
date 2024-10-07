'''A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, 
the next list in the sequence is formed by taking the absolute differences of neighboring integers in the previous list.
Start List: [0,653,1854,4063]
Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]'''
def ducci_sequence(test_list, n):
    # Initialize the sequence with the starting list
    sequence = [test_list]

    # Generate the Ducci sequence
    while True:
        current_list = sequence[-1]
        next_list = [abs(current_list[i] - current_list[(i + 1) % 4]) for i in range(4)]
        sequence.append(next_list)
        if next_list == [0, 0, 0, 0]:
            break

    # Return the nth element of the sequence
    return sequence[n]

# Example usage
test_list = [0, 653, 1854, 4063]
n = 1
ducci_element = ducci_sequence(test_list, n)
print(ducci_element)
