def solve(arr):
    for element in arr:
        arr[arr.index(element)] = ''.join(sorted(set(element)))
    
    sum_positions = []
    already_used = []
    for element in arr:
        if element not in already_used and arr.count(element) > 1:
            sum_positions.append(0)
            next_pos_elem = arr.index(element)
            for i in range(arr.count(element)):
                next_pos_elem = arr.index(element, next_pos_elem + min(1, i))
                sum_positions[-1] += arr.index(element, next_pos_elem)
            already_used.append(element)
                
    return sorted(sum_positions)
