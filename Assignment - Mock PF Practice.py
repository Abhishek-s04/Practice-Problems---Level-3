'''Consider a list (uniquecode_list) containing strings representing unique codes for vehicle identification.
    For Example: 
uniquecode_list: ['AZ01-1234','R137-8714','HR05-2941']
Write a function that takes the uniquecode_list as input and returns another list, 
say rotated_list containing encrypted strings of uniquecode_list. The logic for encryption is based on the two conditions as discussed below:
Unique codes in the uniquecode_list will be in 'XXXX-YYYY' format, where X is alphanumeric and Y is numeric. 
Alphabets in 'XXXX' will always appear at the beginning.
There can be either only one or maximum two alphabets in 'XXXX'

'''
def list_rotate(uniquecode_list):
    rotated_list = []
    
    # Helper function to rotate a string by n positions
    def rotate_string(s, n):
        return s[n:] + s[:n]
    
    for code in uniquecode_list:
        # Split the code into 'XXXX' and 'YYYY' parts
        xxxx, yyyy = code.split('-')
        
        # Count the number of alphabets in 'XXXX'
        num_alphabets = sum(1 for char in xxxx if char.isalpha())
        
        # Rotate 'YYYY' according to the number of alphabets in 'XXXX'
        if num_alphabets == 2:
            # Rotate twice
            rotated_yyyy = rotate_string(yyyy, 2)
        elif num_alphabets == 1:
            # Rotate once
            rotated_yyyy = rotate_string(yyyy, 1)
        
        # Combine 'XXXX' with the rotated 'YYYY'
        rotated_list.append(xxxx + rotated_yyyy)
    
    return rotated_list

# Testing the function with given test case
uniquecode_list = ["AZ01-1234", "R137-8714", "HR05-2941"]
rotated_list = list_rotate(uniquecode_list)
print(rotated_list) 
