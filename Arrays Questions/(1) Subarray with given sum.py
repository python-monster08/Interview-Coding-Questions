def find_subarray_with_sum(arr, target):
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        current_sum += arr[end] 
        
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
            
        if current_sum == target:
            return [start+1, end+1]
            
    return [-1]
    
    # for i in range(len(arr)):
    #     c_sum = 0
    #     print(i,c_sum, "111111111")
    #     for j in range(i, len(arr)):
    #         c_sum += arr[j]
    #         print(j,c_sum,arr[j], "22222222222")
            
    #         if c_sum == target:
    #             return [i+1, j+1]
    #         if c_sum >  target:
    #             break
    # return [-1]

def main():
    # Test cases
    test_cases = [
        ([1, 2, 3, 7, 5], 12),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15),
        ([7, 2, 1], 2),
        ([5, 3, 4], 2),
        ([10, 2, -2, -20, 10], -10),  # Testing negative sums
    ]

    for arr, target in test_cases:
        result = find_subarray_with_sum(arr, target)
        print(f"Array: {arr}, Target: {target} -> Result: {result}")
        
if __name__ == "__main__":
    main()
