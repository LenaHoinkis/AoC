with open('data.txt', 'r') as file:
    lines = file.readlines()

    # idea: find max and then look for the next max on the right side
    # ignore the last x numbers, they will be considered later.
    def find_first_max(l, skip_last):
        return max(enumerate(l[:-1-skip_last]), key=lambda x: x[1])
    
    def calc_jolt(batteries,size):
        numbers = []
        for i in range(size-1, -1, -1):
            index, num = (find_first_max(batteries,i))
            batteries = batteries[index+1:]
            numbers.append(num)
        return int("".join(numbers))

    #part1
    total_jolt = 0
    for line in lines:
        total_jolt += calc_jolt(line,2) 
    print (total_jolt)

    #part2
    total_jolt = 0
    for line in lines:
        total_jolt += calc_jolt(line,12)
    print(total_jolt)
