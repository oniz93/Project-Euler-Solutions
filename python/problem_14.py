start_num = 1
longest_chain = 0
big_num_long_chain = 0
for start_num in range(2, 1000000):
    chain_length = 1
    chain_number = start_num

    while chain_number != 1:
        chain_length += 1
        if chain_number & 1 == 0:
            chain_number >>= 1
        else:
            chain_number = 3 * chain_number + 1

    if longest_chain < chain_length:
        longest_chain = chain_length
        big_num_long_chain = start_num

print("Solution is: " + str(big_num_long_chain))
