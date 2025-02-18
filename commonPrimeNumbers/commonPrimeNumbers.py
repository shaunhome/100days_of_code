list1 = [2, 3, 5, 7, 11]
list2 = [3, 7, 13, 17]

def common_prime_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_set = set1 & set2
    
    common_list = list(common_set)
    return common_list
    

print(common_prime_numbers(list1, list2))