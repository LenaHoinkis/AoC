with open('data.txt', 'r') as file:
    lines = file.readlines()

    # idea: find max and then look for the next max on the right side
    # ignore the last x numbers, they will be considered later.
    def find_first_max(l, skip_last):
        return max(enumerate(l[:-1-skip_last]), key=lambda x: x[1])
    
    #part1
    result = 0
    for line in lines:
        max_index, first_num = find_first_max(line,1) 
        max_index, second_num = find_first_max(line[max_index+1:],0) 
        result+= int(first_num+second_num)
    print (result)

    #part2
    result = 0
    for line in lines:
        numbers = []
        for i in range(11, -1, -1):
            i, num = (find_first_max(line,i))
            line = line[i+1:]
            numbers.append(num)
        result += int("".join(numbers))
    print(result)
