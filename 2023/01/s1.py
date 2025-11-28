with open('data.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        numbers = ''.join(char for char in line if char.isnumeric())
        result += int(numbers[0] + numbers[-1])
    print (result)
