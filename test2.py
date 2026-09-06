# 1. Define the input lists
key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

key2 = ['u', 'b', 'o', 'x', 'e', 'a']
value2 = [200, 30, 10, 88, 55, 920]

# 2. Pair lists into dictionaries
dict1 = {k: v for k, v in zip(key1, value1)}
dict2 = {k: v for k, v in zip(key2, value2)}

# 3. Merge dictionaries while filtering for odd values only
merged_dict = {
    **{k: v for k, v in dict1.items() if v % 2 != 0},
    **{k: v for k, v in dict2.items() if v % 2 != 0}
}

# 4. Display the result
print(merged_dict)