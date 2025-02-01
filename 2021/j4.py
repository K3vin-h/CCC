
def min_swaps(s):
    count_L = s.count('L')
    count_M = s.count('M')
    count_S = s.count('S')
    
    # Define the target sections
    target = ['L'] * count_L + ['M'] * count_M + ['S'] * count_S
    
    # Initialize swap count
    swaps = 0
    
    # Convert string to list for easier manipulation
    s_list = list(s)
    
    for i in range(len(s_list)):
        if s_list[i] != target[i]:
            # Find the correct book to swap with
            for j in range(i+1, len(s_list)):
                if s_list[j] == target[i]:
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    swaps += 1
                    break
    
    return swaps

N = input()
print(min_swaps(N))