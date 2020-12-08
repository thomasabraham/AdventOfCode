from sys import stdin

def solution_sum_two(input_array):
    for i in range(0, len(input_array)):
        for j in range(i+1, len(input_array)):
                if(input_array[i] + input_array[j] == 2020):
                    print("input_array[",i,"] = " , input_array[i])
                    print("input_array[",j,"] = " , input_array[j])
                    print("Sum = " , (input_array[i] + input_array[j]))
                    return input_array[i] * input_array[j] 

# Input length is 200, so loop in a loop in a loop should be fine here.
def solution_sum_three(input_array):
    for i in range(0, len(input_array)):
        for j in range(i+1, len(input_array)):
            for k in range (j+1, len(input_array)):
                if(input_array[i] + input_array[j] + input_array[k] == 2020):
                    print("input_array[",i,"] = " , input_array[i])
                    print("input_array[",j,"] = " , input_array[j])
                    print("input_array[",k,"] = " , input_array[k])
                    print("Sum = " , (input_array[i] + input_array[j] + input_array[k]))
                    return input_array[i] * input_array[j] * input_array[k]

input_array = []

for line in stdin:
    if line == '':
        break;
    input_array.append(int(line))
    
print("Array is ", input_array)
print("Solution for part-1 is ", solution_sum_two(input_array))
print("Solution for part-2 is ", solution_sum_three(input_array))

