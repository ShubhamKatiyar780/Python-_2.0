def power_set(arr):
    if len(arr) == 0:
        return [[]]
    first_element = arr[0]
    remaining_elements = arr[1 : ]
    remaing_power_set = power_set(remaining_elements)
    # print(remaing_power_set, first_element)
    power_set_with_first = []
    for subset in remaing_power_set:
        # print(subset)
        power_set_with_first.append([first_element] + subset)
    return remaing_power_set + power_set_with_first

print(power_set([1,2]))



# l = []
# l.append([1] + [])
# print(l)
