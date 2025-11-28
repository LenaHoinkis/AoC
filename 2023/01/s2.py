with open('data.txt', 'r') as file:
    lines = file.readlines()
    result = 0

    writtenNum = {
            "one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9",
    }

    for line in lines:
        numbers = []
        for i, char in enumerate(line):
            if char.isnumeric() == True:
                numbers.append((i,char))
        for written, num in writtenNum.items():
            start = 0
            while True:
                foundPos = line.find(written, start)
                if foundPos == -1:
                    break
                numbers.append((foundPos, num))
                start = foundPos + 1
        numbers.sort(key=lambda x: x[0])
        print("numbers: {0} and result {1}".format(numbers, int(numbers[0][1] + numbers[-1][1])))
        result += int(numbers[0][1] + numbers[-1][1])
    print (result)
