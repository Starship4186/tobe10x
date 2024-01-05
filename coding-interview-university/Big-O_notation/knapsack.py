# We have a set of numbers
# we have a target value
# We have to find a optimum values from the set which fills the knapsack

S = [  2, 3 , 4 , 7, 8]
# S = [1, 7, 8]
T = 12

S1 = [1, 2, 3]
T1 = 4

S2 = [ 3, 4, 5]
T2 = 7

'''
Does the set has values for filling the knapsack?
1 + 2 + 3
'''

# S.sort()

# temp = 0
# while( temp != T):
#     S_local = S[::-1]
#     tmp = []
#     sum = 0
#     for i in S_local:
#         sum += i
#         tmp.append(i)
#     print(tmp)
#     temp = T

# temp = []
# t = 0
# for i in S:
#     t = t + i

#     if t == T:
#         print(temp)
#         exit

#     if t > T and (t - T) in S:
#         temp.remove(t-T)
#         print(temp)
#         continue
    
#     temp.append(i)
#     print(temp)

# From ChatGPT
# Using recursion
def find_exact_sum(s, target):
    def find_combination(index, current_sum, current_combination):
        if current_sum == target:
            result_combinations.append(list(current_combination))
            return

        if index == len(s) or current_sum > target:
            return

        # Include the current element in the combination
        current_combination.append(s[index])
        find_combination(index + 1, current_sum + s[index], current_combination)

        # Exclude the current element from the combination
        current_combination.pop()
        find_combination(index + 1, current_sum, current_combination)

    result_combinations = []
    find_combination(0, 0, [])

    return result_combinations


# Non recursion - ChatGPT
def find_exact_sum(s, target):
    result_combinations = [[]]
    
    for num in s:
        new_combinations = []
        for combination in result_combinations:
            new_sum = sum(combination)
            if new_sum + num <= target:
                new_combinations.append(combination + [num])

        result_combinations.extend(new_combinations)

    return [combination for combination in result_combinations if sum(combination) == target]


# Example usage
s = [1, 2, 3, 4, 7, 8]
target_sum = 15

result = find_exact_sum(s, target_sum)

if result:
    print(f"Exact sum of {target_sum} can be achieved with the following combinations:")
    for combination in result:
        print(combination)
else:
    print(f"No exact sum of {target_sum} can be achieved with elements from the set.")

